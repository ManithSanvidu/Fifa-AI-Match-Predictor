from fastapi import FastAPI
from pydantic import BaseModel

import sys
import os

sys.path.append(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        "src"
    )
)

from predict import predict_match

app=FastAPI(
    title="FIFA World Cup AI Predictor",
    description="AI Match Outcome Predictor",
    version="1.0"
)

class MatchInput(BaseModel):
    home_rank:float
    away_rank:float
    home_player_rating:float
    away_player_rating:float
    rank_difference:float
    rating_difference:float

@app.get("/")

def home():
    return{
        "message":"FIFA AI Predictor API",
        "status":"Running"
    }

@app.post("/predict")

def predict(data:MatchInput):
    features=[
        data.home_rank,
        data.away_rank,
        data.home_player_rating,
        data.away_player_rating,
        data.rank_difference,
        data.rating_difference
    ]

    result=predict_match(features)

    return result