# gsheets.py
from google.oauth2 import service_account
from googleapiclient.discovery import build
import os

SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

class GoogleSheetsCache:
    def __init__(self, ttl_seconds=300):
        self.ttl = ttl_seconds
        self._cache = {}
        self._last_fetch = 0
        self.sheet_id = os.getenv("GOOGLE_SHEETS_ID")
        # Menggunakan file credentials.json langsung
        self.json_path = os.path.join(os.path.dirname(__file__), 'credentials.json')

    def _get_service(self):
        if not os.path.exists(self.json_path) or not self.sheet_id:
            return None
        creds = service_account.Credentials.from_service_account_file(self.json_path, scopes=SCOPES)
        return build('sheets', 'v4', credentials=creds)