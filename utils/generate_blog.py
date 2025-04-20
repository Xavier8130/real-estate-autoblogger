from huggingface_hub import InferenceClient
import os

def generate_blog(keywords):
    hf_token = os.environ.get("HF_TOKEN")
    if not hf_token:
        raise ValueError("Hugging Face token is missing. Please check your GitHub Secrets.")

    client = InferenceClient(
        model="HuggingFaceH4/zephyr-7b-beta",
        token=hf_token
    )

    prompt = f"""You're a witty, SEO-savvy Gen Z blogger with deep knowledge of UAE real estate.

Write a 700-word blog post using the following trending keywords:
{', '.join(keywords)}.

✅ The blog should:
- Be informative but fun, poetic, and slightly cheeky
- Include subheadings and bullet points
- Sound confident and persuasive
- End with a bold call-to-action like "Book your free consultation today!"

Keep it real estate-focused, Dubai & RAK specific. Let's go!"""

    response = client.text_generation(prompt, max_new_tokens=300, temperature=0.8)

    return response
