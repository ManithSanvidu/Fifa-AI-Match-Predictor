import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_PATH = os.path.join(BASE_DIR, "data")

MODEL_PATH = os.path.join(BASE_DIR, "models")

MATCH_FILE = os.path.join(DATA_PATH, "matches.csv")

PLAYER_FILE = os.path.join(DATA_PATH, "players.csv")

RANKING_FILE = os.path.join(DATA_PATH, "rankings.csv")