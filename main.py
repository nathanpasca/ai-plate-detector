import google.generativeai as genai
from dotenv import load_dotenv
import PIL.Image
import os

load_dotenv()

file = PIL.Image.open("file.jpeg")
api_key = os.getenv("API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest")


prompt = [
    file,
    "You are a parking gate that receives picture and recognize plate number. Recognize the plate number based on from the input picture. Give output with JSON format that gave example output like this {'plat_no': 'B 1234 ABC', 'vehicle': 'car', 'vehicle_type': 'sedan', 'color': 'red', 'gate_open': '2024-12-02 18.15.01', 'gate_closed': 'N/A'",
]

response = model.generate_content(prompt)

print(response.text)
