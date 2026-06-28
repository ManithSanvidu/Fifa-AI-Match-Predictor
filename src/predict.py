import os
import joblib
import numpy as np

from config import MODEL_PATH
from confidence import calculate_confidence


def _load_model(filename):
    path = os.path.join(MODEL_PATH, filename)
    try:
        return joblib.load(path)
    except Exception:
        return None

rf_model = _load_model("rf_model.pkl")
xgb_model = _load_model("xgb_model.pkl")
nn_model = _load_model("nn_model.pkl")
poisson_home = _load_model("poisson_home.pkl")
poisson_away = _load_model("poisson_away.pkl")


def predict_match(features):
    features = np.array(features).reshape(1, -1)

    probabilities = []
    for model in (rf_model, xgb_model, nn_model):
        if model is not None and hasattr(model, "predict_proba"):
            probabilities.append(model.predict_proba(features)[0])

    if probabilities:
        final_prob = np.mean(probabilities, axis=0)
    else:
        final_prob = np.array([1.0 / 3, 1.0 / 3, 1.0 / 3])

    winner = np.argmax(final_prob)
    labels = {0: "Home Win", 1: "Draw", 2: "Away Win"}

    home_goals = (
        float(poisson_home.predict(features)[0])
        if poisson_home is not None and hasattr(poisson_home, "predict")
        else 1.0
    )

    away_goals = (
        float(poisson_away.predict(features)[0])
        if poisson_away is not None and hasattr(poisson_away, "predict")
        else 1.0
    )

    confidence = calculate_confidence(final_prob)

    return {
        "winner": labels[winner],
        "home_win_probability": round(float(final_prob[0] * 100), 2),
        "draw_probability": round(float(final_prob[1] * 100), 2),
        "away_win_probability": round(float(final_prob[2] * 100), 2),
        "predicted_home_goals": round(home_goals, 2),
        "predicted_away_goals": round(away_goals, 2),
        "confidence": confidence,
    }

