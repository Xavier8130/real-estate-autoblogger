from utils.scrape_trends import get_trending_keywords
from utils.generate_blog import generate_blog

if __name__ == "__main__":
    keywords = get_trending_keywords()
    print("🔥 Trending Keywords:", keywords)
    blog_post = generate_blog(keywords)
    print("📄 Blog Post Generated:\n", blog_post)
