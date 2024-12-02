import google.generativeai as genai
from IPython.display import Markdown
from dotenv import load_dotenv
import PIL.Image
import os
import sys
from datetime import datetime


def init_gemini():
    try:
        load_dotenv()
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY not found in environment variables")
        genai.configure(api_key=api_key)
        return genai.GenerativeModel(model_name="gemini-1.5-pro-latest")
    except Exception as e:
        print(f"Error initializing Gemini: {e}")
        sys.exit(1)


def process_image(image_path):
    try:
        file = PIL.Image.open(image_path)
        return file
    except Exception as e:
        print(f"Error loading image: {e}")
        sys.exit(1)


def main():
    # Initialize model
    model = init_gemini()

    # Process image
    image = process_image("file.jpeg")

    try:
        # Create prompt with current timestamp
        current_time = datetime.now().strftime("%Y-%m-%d %H.%M.%S")
        prompt = [
            image,
            f"""You are a parking gate that receives picture and recognize plate number. 
            Recognize the plate number based on from the input picture. 
            Give output with JSON format that gave example output like this 
            {{'plat_no': 'B 1234 ABC', 
              'vehicle': 'car', 
              'vehicle_type': 'sedan', 
              'color': 'red', 
              'gate_open': '{current_time}', 
              'gate_closed': 'N/A'}}""",
        ]

        # Generate response
        response = model.generate_content(prompt)
        print(response.text)

    except Exception as e:
        print(f"Error generating content: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
