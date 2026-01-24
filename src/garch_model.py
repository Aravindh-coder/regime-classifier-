from arch import arch_model
import pandas as pd

def fit_garch(returns):
    returns = returns * 100  # scale for stability

    model = arch_model(
        returns,
        vol="Garch",
        p=1,
        q=1,
        mean="Zero",
        dist="normal"
    )

    result = model.fit(disp="off")
    return result

def extract_volatility(result):
    return result.conditional_volatility
