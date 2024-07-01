from open_ai_client import OpenAIClient, API_KEY, TEST_IMAGE;
from google_drive_client import GoogleDriveClient, CREDENTIALS_PATH;
from google_drive_client import GOOGLE_DRIVE_FOLDER_ID;

if __name__ == "__main__":
    # openAiClient = OpenAIClient(api_key=API_KEY,image_url=TEST_IMAGE)
    # openAiClient.get_image_analysis()

    googleDriveClient = GoogleDriveClient(credentials_path=CREDENTIALS_PATH)
    query = f"'{GOOGLE_DRIVE_FOLDER_ID}' in parents and mimeType='image/heif'"
    response = googleDriveClient.list_files(query=query)
    print(response)