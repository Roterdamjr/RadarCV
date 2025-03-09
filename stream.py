from google import genai

client = genai.Client(api_key="AIzaSyAA4_6qB-yAnwmmutcY4nytgQBlw1YWrtA")

response = client.models.generate_content_stream(
    model="gemini-2.0-flash",
    contents=["Explain how AI works"])
for chunk in response:
    print(chunk.text, end="")