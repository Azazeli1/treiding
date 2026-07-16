from trading_bot.strategy import TradingStrategy


def test_buy_signal_for_strong_uptrend():
    strategy = TradingStrategy(short_window=3, long_window=7)
    prices = [100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120]
    assert strategy.get_signal(prices) == "buy"


def test_sell_signal_for_strong_downtrend():
    strategy = TradingStrategy(short_window=3, long_window=7)
    prices = [120, 118, 116, 114, 112, 110, 108, 106, 104, 102, 100]
    assert strategy.get_signal(prices) == "sell"


def test_hold_signal_for_sideways_market():
    strategy = TradingStrategy(short_window=3, long_window=7)
    prices = [100, 100, 101, 100, 101, 100, 101, 100, 101, 100, 101]
    assert strategy.get_signal(prices) == "hold"


def test_market_analysis_returns_details():
    strategy = TradingStrategy(short_window=3, long_window=7)
    analysis = strategy.analyze_market([100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120])

    assert analysis["signal"] == "buy"
    assert analysis["rsi"] > 50
    assert analysis["trend"] == "up"
