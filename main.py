from fastapi import FastAPI
from typing import List

app = FastAPI()

masters = [
    {"id": 1, "name": "Diana Neylova", "username": "diana.nails", 
     "category": "nails", "district": "Bishkek", "rating": 4.9},
    {"id": 2, "name": "Studio Glow", "username": "glow.studio", 
     "category": "spa", "district": "Bishkek", "rating": 4.7},
]

@app.get("/masters", response_model=List[dict])
def get_masters():
  return masters
