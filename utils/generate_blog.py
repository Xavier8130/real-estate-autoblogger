def generate_blog(keywords):
    # Assuming you use Hugging Face's Inference API to generate the blog
    from huggingface_hub import InferenceApi

    # Use the correct model ID here
    api = InferenceApi(repo_id="your-hugging-face-model-id", token="your-hugging-face-token")

    try:
        # Generate blog content
        response = api(inputs=keywords)
        
        # Check the response format
        if 'generated_text' in response:
            blog_post = response['generated_text']
        else:
            print("Error: Response does not contain 'generated_text'. Here is the full response:")
            print(response)
            raise ValueError("No generated text returned.")

    except Exception as e:
        print(f"Error in blog generation: {e}")
        blog_post = "There was an error generating the blog. Please try again."

    return blog_post
