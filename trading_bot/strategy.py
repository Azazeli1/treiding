class TradingStrategy:
    POPULAR_COINS = [
        "BTC",
        "ETH",
        "BNB",
        "SOL",
        "XRP",
        "ADA",
        "DOGE",
        "TRX",
        "AVAX",
        "LINK",
    ]

    def __init__(self, short_window=3, long_window=7):
        self.short_window = short_window
        self.long_window = long_window

    def _moving_average(self, values, window):
        if len(values) < window:
            return sum(values) / len(values)
        return sum(values[-window:]) / window

    def _rsi(self, prices, period=None):
        if len(prices) < 2:
            return 50

        if period is None:
            period = min(14, max(1, len(prices) - 1))

        deltas = [prices[i] - prices[i - 1] for i in range(1, len(prices))]
        gains = [max(delta, 0) for delta in deltas[-period:]]
        losses = [abs(min(delta, 0)) for delta in deltas[-period:]]

        avg_gain = sum(gains) / period
        avg_loss = sum(losses) / period

        if avg_loss == 0:
            return 100 if avg_gain > 0 else 50

        rs = avg_gain / avg_loss
        return 100 - (100 / (1 + rs))

    def analyze_market(self, prices):
        if len(prices) < 2:
            return {"signal": "hold", "trend": "sideways", "rsi": 50}

        short_avg = self._moving_average(prices, self.short_window)
        long_avg = self._moving_average(prices, self.long_window)
        rsi = self._rsi(prices)
        last_price = prices[-1]
        prev_price = prices[-2]
        price_change = last_price - prev_price

        recent_window = prices[-self.short_window:]
        prev_window = prices[-(self.short_window * 2):-self.short_window]
        if not prev_window:
            prev_window = prices[:-self.short_window]
        recent_avg = sum(recent_window) / len(recent_window)
        prev_avg = sum(prev_window) / len(prev_window)
        momentum = recent_avg - prev_avg

        if abs(price_change) <= 1 and abs(short_avg - long_avg) <= 1 and abs(momentum) <= 1:
            signal = "hold"
            trend = "sideways"
        elif short_avg > long_avg and (rsi >= 55 or price_change > 0) and momentum > 0:
            signal = "buy"
            trend = "up"
        elif short_avg < long_avg and (rsi <= 45 or price_change < 0) and momentum < 0:
            signal = "sell"
            trend = "down"
        else:
            signal = "hold"
            trend = "sideways"

        return {"signal": signal, "trend": trend, "rsi": round(rsi, 2)}

    def get_signal(self, prices):
        return self.analyze_market(prices)["signal"]

    def get_signals_for_coins(self, prices_by_coin):
        return {
            coin: self.get_signal(prices_by_coin[coin])
            for coin in self.POPULAR_COINS
            if coin in prices_by_coin
        }
