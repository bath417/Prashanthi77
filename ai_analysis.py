import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

async def analyze_with_gemini(sector: str, news: list):

    news_text = "\n".join(news)

    prompt = f"""
You are a financial market analyst.

Analyze the following news related to the Indian {sector} sector.

News:
{news_text}

Generate a structured markdown report including:

# Sector Overview
# Current Market Trends
# Key Trade Opportunities
# Risks and Challenges
# Future Outlook
# Conclusion
"""

    try:
        response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {"role": "user", "content": prompt}
    ]
)

        return response.choices[0].message.content

    except Exception as e:
        return f"AI analysis failed: {str(e)}"