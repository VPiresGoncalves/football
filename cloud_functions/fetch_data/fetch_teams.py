from typing import Tuple
import requests
import logging
from config import ENDPOINTS, API_KEY

def fetch_teams(competition_id: int, season: int|None) -> Tuple[dict, set]:
    """
    
    Fetch team data for a given league and season.
    
    Args:
        competition_id (int): The competition ID.
        season (int|None): The season.
    Returns:
        dict: Team data (JSON response) or None if an error occurred.
        set: A set of team IDs in the match.
    """
    url = ENDPOINTS["teams"].format(competition_id=competition_id)
    headers = {"X-Auth-Token": API_KEY}
    params = {"season": season} if season else {}

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()

        team_ids = set()
        for team in data.get("teams", []):
            team_id = team.get("id")
            if team_id:
                team_ids.add(team_id)

        return data, team_ids

    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching team data for {competition_id}, {season}: {e}")
        return None, set()