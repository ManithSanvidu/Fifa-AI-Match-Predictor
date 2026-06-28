import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

from evaluate import evaluate_model

from config import DATA_PATH, MODEL_PATH

DATASET = os.path.join(DATA_PATH, "final_dataset.csv")

print("Loading dataset")

df=pd.read_csv(DATASET)

df=df.dropna()

FEATURES=[
    "home_rank",
    "away_rank",
    "home_player_rating",
    "away_player_rating",
    "rank_difference",
    "rating_difference"
]

TARGET = "result"

X = df[FEATURES]

y=df[TARGET]

X_train,X_test,y_train,y_test=train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

nn_model=Pipeline([
    ("scaler",StandardScaler()),
    ("mlp",MLPClassifier(
        hidden_layer_sizes=(128,64),
        activation="relu",
        solver="adam",
        max_iter=500,
        random_state=42
    ))
])

print("\nTraining Neural Network...")

nn_model.fit(X_train,y_train)

accuracy=evaluate_model(
    nn_model,
    X_test,
    y_test
)

os.makedirs(MODEL_PATH,exist_ok=True)

joblib.dump(
    nn_model,
    os.path.join(MODEL_PATH,"nn_model.pkl")
)


print(f"\nNeural Network Accuracy : {accuracy:.4f}")

print("Model Saved Successfully.")