
# Market Regime Classification Framework

## Overview
This project implements an **advanced market regime detection and classification framework** using
probabilistic and econometric models commonly used in quantitative finance and risk management.

The system identifies **hidden market regimes**, models **volatility clustering**, predicts **regime transitions**, and evaluates **regime-aware trading strategies** through backtesting.  
The project is designed to resemble **real-world quantitative research and trading desk workflows**.

---

## Problem Statement
Financial markets do not operate under a single stable condition. Instead, they transition between
different **regimes** such as low volatility, trending, and crisis periods.  
Accurately identifying and adapting to these regimes is critical for **risk management and strategy performance**.

---

## Objectives
- Research and design a market regime classification framework  
- Detect latent market regimes using **Hidden Markov Models (HMM)**  
- Model volatility clustering using **GARCH**  
- Analyze regime-wise volatility behavior  
- Predict regime transitions  
- Adapt trading strategy and risk dynamically  
- Backtest regime-based strategies  
- Produce reproducible and well-documented outputs  

---

## Methodology

### 1. Market Regime Concept
Market regimes are assumed to be **latent (hidden) states** characterized by distinct statistical
properties of returns and volatility:
- **Low Volatility Regime** – stable markets
- **Medium Volatility Regime** – trending markets
- **High Volatility Regime** – stress or crisis periods

---

### 2. Feature Engineering
The following features are used for regime detection:
- **Log Returns** – time-additive and industry standard
- **Rolling Volatility** – captures volatility clustering
- **Momentum (Rolling Mean)** – differentiates trending vs sideways regimes

---

### 3. Hidden Markov Model (HMM)
A multivariate **Gaussian Hidden Markov Model** is used to:
- Infer hidden market regimes
- Estimate regime transition probabilities
- Classify each time step into a regime

HMM is well-suited because regimes are **not directly observable** and market behavior is probabilistic.

---

### 4. GARCH Volatility Modeling
A **GARCH(1,1)** model is applied to returns to:
- Capture conditional heteroskedasticity
- Model volatility persistence
- Validate volatility clustering across regimes

---

### 5. Volatility Clustering Analysis
Rolling volatility and regime-wise statistics are used to:
- Demonstrate persistence of high-volatility periods
- Compare volatility characteristics across regimes

---

### 6. Regime Prediction
Regime transition probabilities from the HMM are used to:
- Predict the most likely next regime
- Quantify regime persistence and switching behavior

---

### 7. Strategy Adaptation & Risk Scaling
Trading exposure is dynamically adjusted based on detected regimes:
- Higher exposure in low-volatility regimes
- Normal exposure in medium-volatility regimes
- Reduced exposure in high-volatility regimes

This reflects **real-world risk management practices**.

---

### 8. Backtesting
A regime-based strategy is backtested to evaluate:
- Equity curve behavior
- Risk-adjusted performance
- Impact of regime-aware position sizing

---

## Project Structure
regime-classifier/ │ ├── data/ │   └── market_data.csv │ ├── src/ │   ├── data_loader.py │   ├── features.py │   ├── hmm_model.py │   ├── garch_model.py │   ├── clustering.py │   ├── regime_predictor.py │   ├── strategy.py │   ├── backtest.py │   └── app.py │ ├── outputs/ │   ├── output.png │   └── output1.png │ ├── notebooks/ │   └── research.ipynb │ ├── requirements.txt └── README.md
Copy code

---

## Output Visualizations

### Hidden Markov Model – Regime Detection
![HMM Regime Detection](outputs/output.png)

---

### Strategy Performance & Volatility Analysis
![Strategy Performance](outputs/output1.png)

---

## How to Run the Project

### 1. Install Dependencies
```bash
pip install -r requirements.txt
2. Run the Dashboard
Copy code
Bash
streamlit run src/app.py
The dashboard will display:
Detected market regimes
Volatility dynamics
Regime-based strategy performance
Data Source
Market data is programmatically fetched using Yahoo Finance (yfinance) and stored locally to ensure reproducibility and auditability.
Key Insights
Financial markets exhibit persistent regime behavior
Volatility clustering is effectively captured using GARCH models
Regime-aware strategies improve risk control during high-volatility periods
Probabilistic models are suitable for real-world regime classification problems
Limitations
Regime labels are model-dependent and not directly observable
Transaction costs are not included
Model performance depends on chosen features and parameters
Disclaimer
This project is intended for educational and research purposes only and does not constitute financial or investment advice.
Copy code

---

## ✅ FINAL NOTES (IMPORTANT)
- Images **must be pushed** to `outputs/output.png` and `outputs/output1.png`
- Filenames are **case-sensitive**
- README will render images automatically on GitHub (even in private repos)

If you want next:
- 📄 **PDF documentation**
- 📊 **Sharpe ratio / drawdown metrics**
- 🎯 **Interview explanation points**

Just tell me — you’re already at a **very strong submission level** 💪
