from open_ai_client import OpenAIClient, API_KEY, TEST_IMAGE;

if __name__ == "__main__":
    openAiClient = OpenAIClient(api_key=API_KEY,image_url=TEST_IMAGE)
    openAiClient.get_image_analysis()