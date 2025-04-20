from huggingface_hub import InferenceClient
import os

def generate_blog(keywords):
    hf_token = os.environ.get("HF_TOKEN")
    if not hf_token:
        raise ValueError("Hugging Face token is missing. Please check your GitHub Secrets.")

    client = InferenceClient(
        model="tiiuae/falcon-7b-instruct",  # or whatever model you're using
        token=hf_token
    )

    prompt = f"""Write an engaging, SEO-optimized real estate blog article (700 words) for Gen Z investors in the UAE. Use the following trending keywords:
    
    {', '.join(keywords)}

    Structure:
    - Catchy title
    - Short intro
    - Main body with bullet points
    - Call to action at the end
    """

    response = client.text_generation(prompt, max_new_tokens=700)

    return response
