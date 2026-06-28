import numpy as np
import pandas as pd
import random

class TournamentSimulator:
    def __init__(self,models,data):
        self.models=models
        self.data=data

        self.teams=sorted(data["team"].dropna().unique())

    def _get_features(self,team_a,team_b):
        df=self.data

        a_rating=df[df["team"]==team_a]["overall"].mean()
        b_rating=df[df["team"]==team_b]["overall"].mean()

        a_rating=75 if np.isnan(a_rating) else a_rating
        b_rating = 75 if np.isnan(b_rating) else b_rating

        return np.array([[a_rating, b_rating]])

    def predict_match(self,team_a,team_b):
        features=self._get_features(team_a,team_b)

        rf=self.models.get("rf",None)

        if rf:
            probs=rf.predict_proba(features)[0]
            away_win,draw,home_win=probs

        else:
            home_win=random.uniform(0.3,0.5)
            draw=random.uniform(0.2,0.3)
            away_win=1-(home_win+draw)

        outcome=np.argmax([away_win,draw,home_win])

        if outcome==2:
            return team_a
        elif outcome==0:
            return team_b
        else:
            return random.choice([team_a,team_b])

    def simulate_round(self,teams):
        winners = []

        for i in range(0, len(teams), 2):
            team_a = teams[i]
            team_b = teams[i + 1]

            winner = self.predict_match(team_a, team_b)
            winners.append(winner)

        return winners

    def simulate_tournament(self,selected_teams=None):
        if selected_teams is None:
            selected_teams=random.sample(self.teams,16)

        if len(selected_teams) != 16:
            raise ValueError("Tournament requires exactly 16 teams")

        results = {}

        # Round of 16 (initial teams)
        round_of_16 = selected_teams
        results["round_of_16"] = round_of_16

        # Quarter finals (8 teams)
        quarter_finalists = self.simulate_round(round_of_16)
        results["quarter_finals"] = quarter_finalists

        # Semi finals (4 teams)
        semi_finalists = self.simulate_round(quarter_finalists)
        results["semi_finals"] = semi_finalists

        # Final (2 teams)
        finalists = self.simulate_round(semi_finalists)
        results["final"] = finalists

        # Champion (single team)
        champion = self.simulate_round(finalists)[0]
        results["champion"] = champion

        return results

