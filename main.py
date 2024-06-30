from openai import OpenAI
import os

client = OpenAI()
DETAIL_HIGH = "high"
DETAIL_LOW = "low"
GPT_4O = "gpt-4o"
TEST_IMAGE="https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"
API_KEY=os.getenv("OPENAI_API_KEY")

class OpenAIClient:
    
    def __init__(self, api_key: str, image_url: str):
        self.api_key = api_key
        self.image_url = image_url
        self.client = OpenAI(api_key=self.api_key)

    def get_image_analysis(self):
        response = client.chat.completions.create(
            model=GPT_4O,
            messages=[
                {
                "role": "user",
                "content": [
                    {"type": "text", "text": "What’s in this image?"},
                    {
                    "type": "image_url",
                    "image_url": {
                        "url": self.image_url,
                    },
                    },
                ],
                }
            ],
            max_tokens=300,
        )
        print(response.choices[0].message.content)
        # print("Hello World")

if __name__ == "__main__":
    openAiClient = OpenAIClient(api_key=API_KEY,image_url=TEST_IMAGE)
    openAiClient.get_image_analysis()