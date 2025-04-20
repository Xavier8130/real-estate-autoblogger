from huggingface_hub import InferenceClient
import os

def generate_blog(keywords):
    hf_token = os.environ.get("HF_TOKEN")
    
    if not hf_token:
        raise ValueError("Hugging Face token is missing. Please check your GitHub Secrets.")

    client = InferenceClient(model="mistralai/Mistral-7B-Instruct-v0.1", token=hf_token)


    prompt = f"""Write a 700-word SEO-friendly real estate blog using these trending keywords:
    {', '.join(keywords)}
    The tone should be Gen Z + professional. Use subheadings, bullet points, and a clear CTA at the end."""

    response = client.text_generation(prompt, max_new_tokens=350)

    return response
