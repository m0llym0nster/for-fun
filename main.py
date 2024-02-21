#!/usr/bin/python

from fastapi import FastAPI
import pso_sectid
import uvicorn

"""first time using fast api
This API will return the Sector ID based on the name you provide it,
just like PSO ep1 (not blueburst)."""

app = FastAPI()
@app.get("/sectid/{yourname}")
#user must GET request /sectid/ with their name appended
async def read_item(yourname):
    sectorid=pso_sectid.pso_sectid(yourname)
    return { yourname : sectorid }

# with this update below, you just need to run the app and have deps installed. 
# no need to call uvicorn from cli
if __name__ == "__main__":
    #uvicorn.run("main:app", port=8000, log_level=:"info")
    uvicorn.run("main:app", port=8000, host=0.0.0.0, log_level="info")
    server = uvicorn.Server(config)
    server.run()
