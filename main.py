from fastapi import FastAPI
import pso_sectid

"""first time using fast api"""

app = FastAPI()
@app.get("/sectid/{yourname}")
async def read_item(yourname):
    sectorid=pso_sectid.pso_sectid(yourname)
    return { yourname : sectorid }
