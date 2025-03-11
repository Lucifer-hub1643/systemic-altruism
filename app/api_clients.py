import os
import httpx

API_BASE_URL = os.getenv("API_BASE_URL", "https://api.socialverseapp.com")
FLIC_TOKEN = os.getenv("FLIC_TOKEN", "your_flic_token")

headers = {
    "Flic-Token": FLIC_TOKEN
}

async def fetch_viewed_posts():
    url = f"{API_BASE_URL}/posts/view?page=1&page_size=1000"
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
    return response.json()

async def fetch_liked_posts():
    url = f"{API_BASE_URL}/posts/like?page=1&page_size=1000"
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
    return response.json()

# Similarly, implement functions for inspired posts, rated posts, etc.
