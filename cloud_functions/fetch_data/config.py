import os
from dotenv import load_dotenv

load_dotenv()

API_BASE_URL = "https://api.football-data.org/v4"

ENDPOINTS = {
    "matches": f"{API_BASE_URL}/competitions/{{competition_id}}/matches",
    "teams": f"{API_BASE_URL}/competitions/{{competition_id}}/teams",
    "players":f"{API_BASE_URL}/teams/{{team_id}}"
}

API_KEY = os.getenv("API_KEY")

BUCKET_NAME = os.getenv("BUCKET_NAME", "football-raw-data")