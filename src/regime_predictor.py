import numpy as np

def transition_matrix(hmm_model):
    return hmm_model.transmat_

def predict_next_regime(current_regime, transmat):
    return np.argmax(transmat[current_regime])

def regime_probabilities(hmm_model):
    return hmm_model.predict_proba(hmm_model._compute_log_likelihood)
