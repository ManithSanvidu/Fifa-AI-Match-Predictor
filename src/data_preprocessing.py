import pandas as pd

from config import MATCH_FILE
from config import PLAYER_FILE
from config import RANKING_FILE

from utils import save_csv

def preprocess_matches():
    df=pd.read_csv(MATCH_FILE)
    df.columns=df.columns.str.lower()
    df.drop_duplicates(inplace=True)
    df["date"]=pd.to_datetime(df["date"])
    df=df.sort_values("date")
    print("Matches cleaned")
    save_csv(df,MATCH_FILE)
    return df

def preprocess_players():
    df=pd.read_csv(PLAYER_FILE)
    df.columns=df.columns.str.lower()
    df.drop_duplicates(inplace=True)
    df.dropna(subset=["overall"],inplace=True)
    print("Players cleaned")
    save_csv(df,PLAYER_FILE)
    return df

def preprocess_rankings():
    df=pd.read_csv(RANKING_FILE)
    df.columns=df.columns.str.lower()
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)
    print("Rankings cleaned")
    save_csv(df,RANKING_FILE)
    return df

if __name__=="__main__":
    preprocess_matches()
    preprocess_players()
    preprocess_rankings()
    print("Preprocessing completed")
