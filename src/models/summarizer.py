import os 
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("API_KEY")

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-pro")


def summarize_content(text_path, filename):
    data = open(text_path, 'r').read() 
    response = model.generate_content(f"summarize this for me: '{data}'")
    directory = "src/data/output"
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(f"{directory}/{filename}.txt", "w+") as f:
        f.write(response.text)