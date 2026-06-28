import os
import joblib
import pandas as pd
import numpy as np

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models")
DATA_PATH = os.path.join(BASE_DIR, "data")

def load_models():
    models={}

    try:
        models["rf"]=joblib.load(os.path.join(MODEL_PATH,"rf_model.pkl"))
        models["xgb"]=joblib.load(os.path.join(MODEL_PATH,"xgb_model.pkl"))
        models["poisson_home"] = joblib.load(os.path.join(MODEL_PATH, "poisson_home.pkl"))
        models["poisson_away"] = joblib.load(os.path.join(MODEL_PATH, "poisson_away.pkl"))
        models["nn"] = joblib.load(os.path.join(MODEL_PATH, "nn_model.pkl"))

    except Exception as e:
        pass
    return models

def load_data():
    try:
        df = pd.read_csv(os.path.join(DATA_PATH, "final_dataset.csv"))
    except Exception:
        df = pd.DataFrame({
            "home_team": ["Team A"],
            "away_team": ["Team B"],
            "home_rank": [10],
            "away_rank": [20],
            "home_player_rating": [75.0],
            "away_player_rating": [73.0],
            "rank_difference": [-10],
            "rating_difference": [2.0],
            "result": [0]
        })

    return df
def _compute_features(df, home_team, away_team):
    """Build a feature vector [home_rank, away_rank, home_player_rating,
    away_player_rating, rank_difference, rating_difference] for the given
    matchup by averaging historical values from the dataset."""

    FEATURE_COLS = [
        "home_rank", "away_rank",
        "home_player_rating", "away_player_rating",
        "rank_difference", "rating_difference"
    ]
    DEFAULTS = [50.0, 50.0, 75.0, 75.0, 0.0, 0.0]

    # Pull rows where home_team was the home side
    home_rows = df[df["home_team"] == home_team]
    # Pull rows where away_team was the away side
    away_rows = df[df["away_team"] == away_team]

    def avg(series):
        clean = series.dropna()
        return float(clean.mean()) if len(clean) > 0 else None

    home_rank = avg(home_rows["home_rank"]) if "home_rank" in df.columns else None
    away_rank = avg(away_rows["away_rank"]) if "away_rank" in df.columns else None
    home_pr   = avg(home_rows["home_player_rating"]) if "home_player_rating" in df.columns else None
    away_pr   = avg(away_rows["away_player_rating"]) if "away_player_rating" in df.columns else None

    home_rank = home_rank if home_rank is not None else DEFAULTS[0]
    away_rank = away_rank if away_rank is not None else DEFAULTS[1]
    home_pr   = home_pr   if home_pr   is not None else DEFAULTS[2]
    away_pr   = away_pr   if away_pr   is not None else DEFAULTS[3]

    rank_diff   = away_rank - home_rank
    rating_diff = home_pr  - away_pr

    return np.array([[home_rank, away_rank, home_pr, away_pr, rank_diff, rating_diff]])


def predict_match(models, data, home_team, away_team, tournament):
    features = _compute_features(data, home_team, away_team)

    rf = models.get("rf")
    rf_prob = rf.predict_proba(features)[0] if rf else [0.33, 0.34, 0.33]

    home_win = float(rf_prob[0])
    draw     = float(rf_prob[1])
    away_win = float(rf_prob[2])

    winner = (
        "Home Win" if home_win > max(draw, away_win)
        else "Draw"  if draw     > away_win
        else "Away Win"
    )

    return {
        "home_win": home_win,
        "draw":     draw,
        "away_win": away_win,
        "winner":   winner
    }