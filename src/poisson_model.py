import os
import joblib
import pandas as pd

from sklearn.linear_model import PoissonRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

from config import DATA_PATH, MODEL_PATH

DATASET = os.path.join(DATA_PATH, "final_dataset.csv")

FEATURES = [
    "home_rank",
    "away_rank",
    "home_player_rating",
    "away_player_rating",
    "rank_difference",
    "rating_difference",
]

HOME_TARGET = "home_score"
AWAY_TARGET = "away_score"


def train_poisson_models():
    df = pd.read_csv(DATASET).dropna()
    X = df[FEATURES]
    y_home = df[HOME_TARGET]
    y_away = df[AWAY_TARGET]

    X_train, X_test, y_home_train, y_home_test = train_test_split(
        X,
        y_home,
        test_size=0.20,
        random_state=42,
    )

    _, _, y_away_train, y_away_test = train_test_split(
        X,
        y_away,
        test_size=0.20,
        random_state=42,
    )

    print("\nTraining Home Goal Poisson Model...")
    home_model = PoissonRegressor(max_iter=500)
    home_model.fit(X_train, y_home_train)
    home_predictions = home_model.predict(X_test)
    home_mae = mean_absolute_error(y_home_test, home_predictions)
    print(f"Home Goal MAE: {home_mae:.3f}")

    print("\nTraining Away Goal Poisson Model...")
    away_model = PoissonRegressor(max_iter=500)
    away_model.fit(X_train, y_away_train)
    away_predictions = away_model.predict(X_test)
    away_mae = mean_absolute_error(y_away_test, away_predictions)
    print(f"Away Goal MAE: {away_mae:.3f}")

    return home_model, away_model


def save_poisson_models(home_model, away_model):
    os.makedirs(MODEL_PATH, exist_ok=True)
    joblib.dump(home_model, os.path.join(MODEL_PATH, "poisson_home.pkl"))
    joblib.dump(away_model, os.path.join(MODEL_PATH, "poisson_away.pkl"))


if __name__ == "__main__":
    home_model, away_model = train_poisson_models()
    save_poisson_models(home_model, away_model)
    print("\nPoisson models saved successfully.")