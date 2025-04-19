from dotenv import load_dotenv
import os
from huggingface_hub import InferenceApi

load_dotenv()

HUGGINGFACE_TOKEN = os.getenv("HUGGINGFACE_TOKEN")

def generate_blog(keywords):
    if not HUGGINGFACE_TOKEN:
        raise ValueError("No HuggingFace API token found. Please add your token to the .env file.")

    api = InferenceApi(repo_id="EleutherAI/gpt-neo-2.7B", token=HUGGINGFACE_TOKEN)

    prompt = f"Write a compelling, SEO-friendly blog post about Dubai or Ras Al Khaimah real estate focusing on the following trending keywords: {', '.join(keywords)}."

    result = api(inputs=prompt)
    return result['generated_text']
