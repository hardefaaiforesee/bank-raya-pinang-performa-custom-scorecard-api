# Libraries
from fastapi import FastAPI
from features import behavior_pillar, capacity_pillar, identity_pillar
import json
import pickle
import uvicorn

# Swagger Documentation
app = FastAPI(
    title = "Bank Raya Pinang Performa Custom Scorecard API",
    description = "This is a documentation for Bank Raya Pinang Performa Custom Scorecard by AIForesee Data Team.",
    version = "0.0.0"
)

@app.get("/")
async def read_root():
    return {"message": "This is The World!"}

# Main
# bikin template json input
# nerima input json nama + npwp + no hp terus scoring pake model

# if __name__ == "__main__":
#     uvicorn.run(app, host = "0.0.0.0", port = 443)