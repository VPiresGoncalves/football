from typing import Tuple
import requests
import logging
from config import ENDPOINTS, API_KEY

def fetch_matches(competition_id: int, season: int) -> Tuple[dict, set]:
    """
    Fetch match data for a given league and season.

    Args:
        competition_id (int): The competition ID.
        season (int): The season.

    Returns:
        dict: Match data (JSON response) or None if an error occurred.
        set: A set of team IDs in the match.
    """
    url = ENDPOINTS["matches"].format(competition_id=competition_id)
    headers = {"X-Auth-Token": API_KEY}
    params = {"season": season}

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()

        team_ids = set()
        for match in data.get("matches", []):
            home_team = match.get("homeTeam", {}).get("id")
            away_team = match.get("awayTeam", {}).get("id")

            if home_team:  # ✅ Ensure the key exists before adding
                team_ids.add(home_team)
            if away_team:
                team_ids.add(away_team)

        return data, team_ids

    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching match data for {competition_id}, {season}: {e}")    
        return None, set()
