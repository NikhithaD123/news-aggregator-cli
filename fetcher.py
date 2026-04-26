import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("NEWS_API_KEY")

def fetch_news(keyword=None, source=None, from_date=None):
    url = "https://newsapi.org/v2/everything"
    params = {
        "apiKey": API_KEY,
        "q": keyword or "technology",
        "sources": source or "",
        "from": from_date or "",
        "pageSize": 20,
        "language": "en"
    }
    params = {k: v for k, v in params.items() if v}
    response = requests.get(url, params=params)
    data = response.json()

    articles = []
    for a in data.get("articles", []):
        articles.append({
            "title": a["title"],
            "source": a["source"]["name"],
            "publishedAt": a["publishedAt"],
            "url": a["url"],
            "description": a.get("description", "")
        })
    return articles