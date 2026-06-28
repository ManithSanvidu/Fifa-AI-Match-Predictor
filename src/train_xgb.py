import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split

from xgboost import XGBClassifier

from evaluate import evaluate_model

from config import DATA_PATH, MODEL_PATH

DATASET = os.path.join(DATA_PATH, "final_dataset.csv")

print("loading dataset...")

df=pd.read_csv(DATASET)

FEATURES=[
    "home_rank",
    "away_rank",
    "home_player_rating",
    "away_player_rating",
    "rank_difference",
    "rating_difference"
]

TARGET="result"

df=df.dropna()

X=df[FEATURES]

y=df[TARGET]

X_train,X_test,y_train,y_test=train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining XGBoost")

xgb_model=XGBClassifier(
    n_estimators=500,
    max_depth=6,
    learning_rate=0.05,
    random_state=42
)

xgb_model.fit(
    X_train,
    y_train
)

accuracy=evaluate_model(
    xgb_model,
    X_test,
    y_test
)

os.makedirs(MODEL_PATH, exist_ok=True)

joblib.dump(
    xgb_model,
    os.path.join(MODEL_PATH, "xgb_model.pkl")
)

print("\nXGBoost Model Saved")

print(f"Accuracy = {accuracy: 4f}")

