import os
from huggingface_hub import InferenceApi

# Fetch the Hugging Face token from environment variables
token = os.getenv('HUGGINGFACE_TOKEN')

# Ensure the token is valid before proceeding
if not token:
    raise ValueError("Hugging Face token is missing. Please check your .env file or GitHub Secrets.")

# Correct model ID
model_id = "huggingface/gpt-3"  # Replace this with the correct model ID

api = InferenceApi(repo_id=model_id, token=token)

# Your code to generate the blog...
