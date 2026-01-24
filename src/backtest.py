import numpy as np
import pandas as pd

def backtest_strategy(returns, positions):
    strat_returns = returns.values * positions
    equity_curve = (1 + strat_returns).cumprod()
    return equity_curve
