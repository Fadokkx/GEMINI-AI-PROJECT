from google import genai 
from google.genai.types import HttpOptions
import os

class teste:
    def teste():
        try:
            print("Olá Mundo")
        except:
            pass

chaveAPI = os.getenv("GEMINI_API_KEY")


client = genai.Client(http_options=HttpOptions(api_version="v1"))

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=f"Qual o último jogo de copa do mundo de clubes FIFA realizada em 2025 ?",
)
print(response.text)
