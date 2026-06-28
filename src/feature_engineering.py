import os
import pandas as pd

from config import MATCH_FILE
from config import PLAYER_FILE
from config import RANKING_FILE
from config import DATA_PATH


matches = pd.read_csv(MATCH_FILE)

players = pd.read_csv(PLAYER_FILE, low_memory=False)

rankings = pd.read_csv(RANKING_FILE)
rankings = rankings.sort_values(["country", "fifa_version"]).drop_duplicates("country", keep="last")

def create_match_result(row):
    if row["home_score"]>row["away_score"]:
        return 0
    elif row["home_score"]==row["away_score"]:
        return 1
    else:
        return 2

matches["result"]=matches.apply(create_match_result,axis=1)

rankings = rankings.rename(
    columns={
        "country": "team",
        "avg_overall": "ranking"
    }
)

matches = matches.merge(

    rankings[["team", "ranking"]],

    left_on="home_team",

    right_on="team",

    how="left"

)

matches.rename(
    columns={"ranking":"home_rank"},
    inplace=True
)

matches.drop(columns=["team"], inplace=True)


matches = matches.merge(

    rankings[["team", "ranking"]],

    left_on="away_team",

    right_on="team",

    how="left"

)

matches.rename(

    columns={"ranking": "away_rank"},

    inplace=True

)

matches.drop(columns=["team"], inplace=True)

player_avg=(
    players.groupby("nationality_name")["overall"]
    .mean()
    .reset_index()
)

player_avg.columns=[
    "team",
    "avg_player_rating"
]

matches = matches.merge(

    player_avg,

    left_on="home_team",

    right_on="team",

    how="left"

)

matches.rename(

    columns={

        "avg_player_rating": "home_player_rating"

    },

    inplace=True

)

matches.drop(columns=["team"], inplace=True)


matches = matches.merge(

    player_avg,

    left_on="away_team",

    right_on="team",

    how="left"

)

matches.rename(

    columns={

        "avg_player_rating": "away_player_rating"

    },

    inplace=True

)

matches.drop(columns=["team"], inplace=True)

matches["rank_difference"] = (
    matches["away_rank"]
    - matches["home_rank"]
)

matches["rating_difference"] = (
    matches["home_player_rating"]
    - matches["away_player_rating"]
)

matches["goal_difference"] = (
    matches["home_score"]
    - matches["away_score"]
)

matches.to_csv(
    os.path.join(DATA_PATH, "final_dataset.csv"),
    index=False
)

print(matches.head())

print()

print("Feature Engineering Completed")

print()

print("final_dataset.csv created successfully")