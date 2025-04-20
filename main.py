from utils.scrape_trends import get_trending_keywords
from utils.generate_blog import generate_blog

if __name__ == "__main__":
    keywords = get_trending_keywords()
    print("🔥 Trending Keywords:", keywords)
    blog_post = generate_blog(keywords)
    print("📄 Blog Post Generated:\n", blog_post)
# Save blog post to a file
import datetime
today = datetime.date.today()
filename = f"blog_posts/{today}-blog.txt"

# Create folder if it doesn't exist
import os
os.makedirs("blog_posts", exist_ok=True)

with open(filename, "w", encoding="utf-8") as f:
    f.write(blog_post)
