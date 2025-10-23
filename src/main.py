import json
from fastapi import FastAPI
from src.make_stats import open_csv
from matplotlib import pyplot as plt


app = FastAPI()

@app.get('/health')
async def health():
    return {"status": "ok"}

@app.get('/stats')
async def stats():
    with open('stats.json', 'r', encoding='utf-8') as read:
        return json.load(read)
        
           
@app.post('/sum')
async def sum_values(x:int, y:int) -> dict:
    sum_values = x+y
    return {'Soma': sum_values} 