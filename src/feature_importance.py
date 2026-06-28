import joblib
import pandas as pd
import matplotlib.pyplot as plt


FEATURES = [
    "home_rank",
    "away_rank",
    "home_player_rating",
    "away_player_rating",
    "rank_difference",
    "rating_difference"
]


model = joblib.load("../models/rf_model.pkl")


importance = model.feature_importances_


df = pd.DataFrame(
    {
        "Feature": FEATURES,
        "Importance": importance
    }
)


df = df.sort_values(
    by="Importance",
    ascending=False
)


print(df)


plt.figure(figsize=(8,5))

plt.bar(
    df["Feature"],
    df["Importance"]
)

plt.xticks(rotation=45)

plt.title("Feature Importance")

plt.tight_layout()

plt.show()