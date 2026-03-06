from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.responses import PlainTextResponse
from slowapi.middleware import SlowAPIMiddleware
from slowapi.errors import RateLimitExceeded
from slowapi import _rate_limit_exceeded_handler

from security import verify_api_key
from rate_limiter import limiter
from data_collector import fetch_sector_news
from ai_analysis import analyze_with_gemini
from utils import validate_sector, track_user_request, get_timestamp

import logging

app = FastAPI(title="Trade Opportunities API")
from datetime import datetime

start_time = datetime.now()

@app.get("/health")
async def health_check():
    uptime = datetime.now() - start_time
    return {
        "status": "API running",
        "service": "Trade Opportunities API",
        "uptime": str(uptime)
    }

logging.basicConfig(level=logging.INFO)

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.add_middleware(SlowAPIMiddleware)

@app.get("/analyze/{sector}", response_class=PlainTextResponse)
@limiter.limit("5/minute")
async def analyze_sector(
    request: Request,
    sector: str,
    user: str = Depends(verify_api_key)
):

    validate_sector(sector)

    try:
        logging.info(f"User requested analysis for sector: {sector}")

        # Track session usage
        request_count = track_user_request(user)

        # Collect data
        news_data = await fetch_sector_news(sector)

        # Generate analysis
        analysis = await analyze_with_gemini(sector, news_data)

        timestamp = get_timestamp()

        final_report = f"""
Generated At: {timestamp}
User Requests Made: {request_count}

{analysis}
"""

        return final_report

    except Exception as e:
        logging.error(f"Analysis failed: {str(e)}")
        raise HTTPException(status_code=500, detail="Analysis failed")