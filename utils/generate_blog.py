import os
from huggingface_hub import InferenceApi

# Load Hugging Face token from GitHub secret
token = os.getenv("HUGGINGFACE_TOKEN")

# Check if token is missing
if not token:
    raise ValueError("Hugging Face token is missing. Please check your .env file or GitHub Secrets.")

# Replace with actual model ID you're using (for example below)
model_id = "mistralai/Mixtral-8x7B-Instruct-v0.1"

api = InferenceApi(repo_id=model_id, token=token)

def generate_blog(keywords):
    prompt = f"Write a blog post about the following real estate topics in Dubai:\n\n{', '.join(keywords)}"
    result = api(inputs=prompt)

    return result.get('generated_text', '🤷 No blog generated.')
