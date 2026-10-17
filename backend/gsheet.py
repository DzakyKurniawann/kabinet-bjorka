import time
import json
import os
from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

class GoogleSheetsCache:
    def __init__(self, ttl_seconds=300):
        self.ttl = ttl_seconds
        self._cache = {}
        self._last_fetch = 0
        self.sheet_id = os.getenv("GOOGLE_SHEETS_ID")
        self.creds_json = os.getenv("GOOGLE_SERVICE_ACCOUNT_JSON")

    def _get_service(self):
        if not self.creds_json or not self.sheet_id:
            return None
        info = json.loads(self.creds_json)
        creds = service_account.Credentials.from_service_account_info(info, scopes=SCOPES)
        return build('sheets', 'v4', credentials=creds)

    def get_payment_records(self, range_name="Kas!A2:E"):
        now = time.time()
        if self._cache and (now - self._last_fetch < self.ttl):
            return self._cache.get("payments", [])

        service = self._get_service()
        if not service:
            return self._cache.get("payments", [])

        try:
            sheet = service.spreadsheets()
            result = sheet.values().get(spreadsheetId=self.sheet_id, range=range_name).execute()
            rows = result.get('values', [])
            
            payments = []
            for row in rows:
                if len(row) >= 4:
                    payments.append({
                        "nim": row[0],
                        "nama": row[1],
                        "bulan": row[2],
                        "status": row[3],
                        "nominal": row[4] if len(row) > 4 else "Rp 50.000"
                    })

            self._cache["payments"] = payments
            self._last_fetch = now
            return payments
        except Exception as err:
            print(f"Error pembacaan Google Sheets: {err}")
            return self._cache.get("payments", [])
        