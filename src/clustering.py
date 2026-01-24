import numpy as np
import pandas as pd

def rolling_volatility(returns, window=20):
    return returns.rolling(window).std()

def volatility_regime_stats(df, regime_col="Regime"):
    stats = df.groupby(regime_col)['Returns'].agg(
        mean_return="mean",
        volatility="std",
        count="count"
    )
    return stats
