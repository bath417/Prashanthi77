# Trade Opportunities API

## INTRODUCTION

Hi Team,
I have implemented a FastAPI-based backend service for generating market analysis reports for different sectors in the Indian economy. The application follows the assignment requirements including data collection, AI-based analysis, authentication, rate limiting, and input validation.

The API accepts a sector name (for example: agriculture, pharmaceuticals, technology) and generates a structured markdown report containing:

* Sector Overview
* Current Market Trends
* Key Trade Opportunities
* Risks and Challenges
* Future Outlook

The system collects sector-related information from online sources and uses an AI language model to generate the analysis report.

---

# Table of Contents

* Introduction
* System Architecture
* Application Flow
* To Run the Application Locally
* Backend Framework
* Session Management
* Rate Limiting
* Security Best Practices
* Input Validation
* AI/Data Sources
* Storage
* API Specification
* Technologies Used

---

# System Architecture

Client Request
↓
FastAPI Endpoint
↓
Authentication & Rate Limiting
↓
Market Data Collection
↓
AI Analysis Engine
↓
Markdown Report Generation
↓
API Response

---

# Application Flow

1. The client sends a request to `/analyze/{sector}`.
2. The API validates the sector input.
3. API key authentication is verified.
4. Rate limiting checks are applied.
5. Market data is collected using web search queries.
6. The collected data is sent to the AI model.
7. The AI model generates a structured report.
8. The API returns the markdown analysis report.

---

# To Run the Application Locally

### Prerequisites

* Python 3.9+
* pip

### Installation

Install dependencies:

pip install -r requirements.txt

### Configure Environment Variables

Create a `.env` file and add:

SECRET_KEY=test123
GROQ_API_KEY=your_api_key

### Run the Server

uvicorn main:app --reload

---

# Backend Framework

Library: **FastAPI**

FastAPI is used as the backend framework for building the REST API service. It provides asynchronous request handling, automatic documentation, and high performance.

---

# Session Management

The system tracks user requests in memory. Session information is maintained using Python variables during runtime without using a database.

---

# Rate Limiting

Library: **SlowAPI**

Rate limiting restricts the number of API requests a user can make within a certain time window to prevent abuse.

---

# Security Best Practices

### Authentication

API key authentication is implemented using request headers.

Example:

x-api-key: test123

### Error Handling

FastAPI HTTPException is used to handle API errors gracefully.

---

# Input Validation

Library: **Pydantic**

Input validation ensures that only valid sector names are accepted by the API.

---

# AI/Data Sources

### AI Model

The system uses **Groq Llama-3.1** to generate structured market analysis reports.

### Web Data Collection

Sector-related market information is collected using web search queries and processed before sending it to the AI model.

---

# Storage

The application uses **in-memory storage**. No external database is required.

---

# API Specification

### Analyze Sector

GET /analyze/{sector}

Example:

GET /analyze/agriculture

Headers:

x-api-key: test123

---

# API Documentation

FastAPI automatically generates API documentation.

Open in browser:

http://127.0.0.1:8000/docs

---

# Technologies Used

* Python
* FastAPI
* Groq LLM
* BeautifulSoup
* HTTPX
* SlowAPI
* Uvicorn

---

# Conclusion

This project demonstrates how a backend API can integrate web data collection, AI-powered analysis, and secure API design to generate trade opportunity insights for different sectors.
