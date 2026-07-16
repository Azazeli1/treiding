# Главный файл запуска бота
# Запуск: python run_bot.py

from trading_bot.strategy import TradingStrategy
from config import COINS


if __name__ == "__main__":
    strategy = TradingStrategy()

    # Здесь нужно подставить реальные данные цен
    # В будущем вместо этого будет подключение к Binance API
    sample_prices = {
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

    # Оставляем только те монеты, которые есть в списке COINS
    filtered = {coin: sample_prices[coin] for coin in COINS if coin in sample_prices}

    print("Сигналы по монетам:")
    for coin, prices in filtered.items():
        analysis = strategy.analyze_market(prices)
        print(f"{coin}: {analysis['signal']} | trend={analysis['trend']} | rsi={analysis['rsi']}")
