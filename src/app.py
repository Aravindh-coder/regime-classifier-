import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

from data_loader import load_market_data
from features import create_features
from hmm_model import train_hmm
from garch_model import fit_garch, extract_volatility
from strategy import regime_based_position
from backtest import backtest_strategy

st.set_page_config(page_title="Regime Classification Dashboard", layout="wide")
st.title("📈 Market Regime Classification & Volatility Analysis")

# -------------------------
# Load Data
# -------------------------
data = load_market_data()
features = create_features(data)

# -------------------------
# HMM REGIME DETECTION
# -------------------------
model, regimes = train_hmm(features.values)
features["Regime"] = regimes

# --- Plot HMM regimes ---
fig1, ax1 = plt.subplots(figsize=(12,5))
scatter = ax1.scatter(
    features.index,
    data.loc[features.index, "Close"],
    c=regimes,
    cmap="viridis",
    s=10
)
ax1.set_title("Hidden Markov Model Regime Detection")
plt.colorbar(scatter, ax=ax1)

plt.savefig("outputs/hmm_regimes.png", dpi=300, bbox_inches="tight")
st.subheader("HMM Detected Regimes")
st.pyplot(fig1)

# -------------------------
# GARCH VOLATILITY
# -------------------------
garch_result = fit_garch(data.loc[features.index, "Returns"])
volatility = extract_volatility(garch_result)

fig2, ax2 = plt.subplots(figsize=(12,4))
ax2.plot(volatility, label="Conditional Volatility")
ax2.set_title("GARCH(1,1) Conditional Volatility")
ax2.legend()

plt.savefig("outputs/garch_volatility.png", dpi=300, bbox_inches="tight")
st.subheader("GARCH Volatility Clustering")
st.pyplot(fig2)

# -------------------------
# STRATEGY BACKTEST
# -------------------------
positions = regime_based_position(
    data.loc[features.index, "Returns"],
    regimes
)

equity_curve = backtest_strategy(
    data.loc[features.index, "Returns"],
    positions
)

fig3, ax3 = plt.subplots(figsize=(12,4))
ax3.plot(equity_curve, label="Regime-Based Strategy")
ax3.set_title("Strategy Equity Curve")
ax3.legend()

plt.savefig("outputs/strategy_equity_curve.png", dpi=300, bbox_inches="tight")
st.subheader("Regime-Based Strategy Performance")
st.pyplot(fig3)

st.success("✅ All output images saved to outputs/ folder")
