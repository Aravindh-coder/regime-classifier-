import pandas as pd
import numpy as np

def log_returns(close_prices):
    """
    Compute log returns.
    Preferred in financial modeling due to time additivity.
    """
    return np.log(close_prices / close_prices.shift(1))


def rolling_volatility(returns, window=20):
    """
    Rolling volatility (standard deviation of returns).
    Captures volatility clustering.
    """
    return returns.rolling(window).std()


def rolling_mean(returns, window=20):
    """
    Rolling mean of returns.
    Helps identify trending vs mean-reverting regimes.
    """
    return returns.rolling(window).mean()


def create_features(df, window=20):
    """
    Master feature engineering function.
    Returns a clean DataFrame ready for HMM / ML models.
    """

    df = df.copy()

    # Core features
    df["LogReturns"] = log_returns(df["Close"])
    df["Volatility"] = rolling_volatility(df["LogReturns"], window)
    df["Momentum"] = rolling_mean(df["LogReturns"], window)

    # Drop NaNs from rolling calculations
    df.dropna(inplace=True)

    # Final feature matrix
    features = df[["LogReturns", "Volatility", "Momentum"]]

    return features
