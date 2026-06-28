import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

from evaluate import evaluate_model
from config import DATA_PATH, MODEL_PATH

DATASET = os.path.join(DATA_PATH, "final_dataset.csv")

print("Loading dataset...")

df = pd.read_csv(DATASET)

print(df.head())

FEATURES = [
    "home_rank",
    "away_rank",
    "home_player_rating",
    "away_player_rating",
    "rank_difference",
    "rating_difference"
]


TARGET = "result"

df=df.dropna()

X=df[FEATURES]

y=df[TARGET]

print("\nDataset Shape")
print(X.shape)

X_train,X_test,y_train,y_test=train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nTraining Random Forest")


rf_model=RandomForestClassifier(
    n_estimators=500,
    max_depth=10,
    random_state=42
)

rf_model.fit(X_train,y_train)

accuracy=evaluate_model(
    rf_model,
    X_test,
    y_test
)

os.makedirs(MODEL_PATH,exist_ok=True)

joblib.dump(
    rf_model,
    os.path.join(MODEL_PATH,"rf_model.pkl")
)

print("\nModel Saved Successfully")

print(f"Accuracy = {accuracy:.4f}")