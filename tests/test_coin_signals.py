from trading_bot.strategy import TradingStrategy


def test_generate_signals_for_top_ten_coins():
    strategy = TradingStrategy()
    prices = {
        "BTC": [100, 102, 104, 103],
        "ETH": [50, 49, 48, 47],
        "BNB": [300, 305, 310, 309],
        "SOL": [20, 21, 22, 21],
        "XRP": [0.5, 0.51, 0.52, 0.53],
        "ADA": [0.4, 0.39, 0.38, 0.37],
        "DOGE": [0.08, 0.09, 0.1, 0.11],
        "TRX": [0.1, 0.11, 0.12, 0.13],
        "AVAX": [15, 14, 13, 12],
        "LINK": [7, 7.2, 7.4, 7.3],
    }

    signals = strategy.get_signals_for_coins(prices)

    assert set(signals.keys()) == {
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
    }
    assert signals["BTC"] == "buy"
    assert signals["ETH"] == "sell"
