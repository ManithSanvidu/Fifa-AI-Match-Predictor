import requests

url = "http://127.0.0.1:8000/predict"

payload = {
    "home_rank": 2,
    "away_rank": 10,
    "home_player_rating": 88,
    "away_player_rating": 81,
    "rank_difference": -8,
    "rating_difference": 7
}

response = requests.post(url, json=payload)

print(response.json())