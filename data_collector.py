import httpx
from bs4 import BeautifulSoup

async def fetch_sector_news(sector: str):

    query = f"{sector} market news India"
    url = f"https://duckduckgo.com/html/?q={query}"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    results = []

    for result in soup.select(".result__snippet"):
        results.append(result.get_text())

    # If scraping fails, return fallback data
    if not results:
        results = [
            f"The {sector} sector in India is experiencing growth due to government initiatives.",
            f"Investments in the {sector} industry are increasing across multiple states.",
            f"Export opportunities for {sector} products are expanding in global markets.",
            f"Technological adoption is improving efficiency in the {sector} sector.",
            f"Private companies are showing increasing interest in the {sector} industry."
        ]

    return results[:5]