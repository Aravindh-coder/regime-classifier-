import numpy as np

def risk_multiplier(regime):
    if regime == 0:
        return 1.5
    elif regime == 1:
        return 1.0
    else:
        return 0.3

def regime_based_position(returns, regimes):
    positions = []
    for r in regimes:
        positions.append(risk_multiplier(r))
    return np.array(positions)
