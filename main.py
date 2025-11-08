''''
A simple FastAPI microservice that:
Exposes /quote endpoint
Returns an inspirational quote (from a small curated list or using OpenAI-style random generation logic)
Logs every API hit in memory (to simulate analytics)
Has a clean JSON API response like:

{
  "quote": "Stay curious, keep building.",
  "author": "AI Bot",
  "timestamp": "2025-11-08T20:15:33Z"
}
'''

from fastapi import FastAPI
from datetime import datetime
import random 

app = FastAPI(title="AI Quote Generator API")

QUOTES =[
    {"quote": "stay curious, keep building.", "author": "Sam"},
    {"quote": "Dream big , start small, act now.", "author":"Simon sinek"},
    {"quote": "Code. Deploy. Repeat.", "author": "DevOps Whisper"},
    {"quote": "The Best way to predict the future is to build it.", "author":"Peter Drucker"},
    {"quote": "Learn fast, fail faster, adapt quickest", "author": "Tech Monk"},
    {"quote": "Where there is Righteoness in heart there is a beauty in character","author":"Dr APJ Kalam"}
]

API_HITS = 0 # for fun analytics

@app.get("/")
def home():
    return {"message": "Welcome to AI Quote Generator API","endpoints":["/quote","/stats"]}

@app.get("/quote")
def get_quote():
    global API_HITS
    API_HITS += 1
    quote = random.choice(QUOTES)
    return {
        "quote": quote["quote"],
        "author": quote["author"],
        "timestamp": datetime.utcnow().isoformat(),
        "api_hits": API_HITS
    }

@app.get("/stats")
def get_stats():
    return {"total_api_hits": API_HITS, "available_quotes": len(QUOTES)}

'''
Explanation 
    /quote -> returns a random quote
    /stats -> shows total API calls(simulated analytics)
    / -> intro endpoint
    ALL data is in memory (no DB for now)

uvicorn main:app --reload
Then visit → http://127.0.0.1:8000/quote
'''