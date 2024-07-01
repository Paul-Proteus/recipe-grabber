import json
from google.oauth2 import service_account
from googleapiclient.discovery import build

CREDENTIALS_PATH = '/Users/dylanb/codebase/recipe-grabber/credentials/luna-love-more-ed680a0f7565.json'

class GoogleDriveClient:
    def __init__(self, credentials_path: str):
        self.credentials_path = credentials_path
        self.credentials = self._load_credentials()
        self.client = self._create_client()

    def _load_credentials(self):
        with open(self.credentials_path, 'r') as f:
            return json.load(f)

    def _create_client(self):
        credentials = service_account.Credentials.from_service_account_info(self.credentials)
        return build('drive', 'v3', credentials=credentials)

    def list_files(self, query: str):
        return self.client.files().list(q=query).execute()
    
if __name__ == "__main__":
    try:
        googleDriveClient = GoogleDriveClient(credentials_path=CREDENTIALS_PATH)
        response = googleDriveClient.list_files(query="mimeType='image/jpeg'")
        print(response)
    except Exception as e:
        print(e)