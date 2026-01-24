import yfinance as yf
import pandas as pd
import os

def load_market_data(
    symbol="^NSEI",
    start="2015-01-01",
    path="data/market_data.csv"
):
    # Download data
    df = yf.download(symbol, start=start)

    # Keep required columns
    df = df[['Open', 'High', 'Low', 'Close', 'Volume']]
    df.dropna(inplace=True)

    # Save to CSV if not exists
    if not os.path.exists(path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        df.to_csv(path)

    # Compute returns
    df['Returns'] = df['Close'].pct_change()
    df.dropna(inplace=True)

    return df
