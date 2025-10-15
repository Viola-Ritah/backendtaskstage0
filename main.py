from fastapi import FastAPI
from pydantic import BaseModel
import requests
from datetime import datetime, timezone
from fastapi.responses import JSONResponse


class User(BaseModel):
    email: str
    name: str
    stack: str




app = FastAPI()

CAT_FACT_URL = "https://catfact.ninja/fact"

@app.get("/me", response_class=JSONResponse)
def get_profile():
    try:
        response = requests.get(CAT_FACT_URL, timeout=5)
        response.raise_for_status()
        cat_fact = response.json().get("fact", "Cats are awesome")

        current_utc_time = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
    except requests.exceptions.RequestException:
        cat_fact = "Could not fetch cat fact at the moment. Try again later."



    profile_data = {
          "status": "success",
        "user": {
            "email": "wakooliviola138@gmail.com",
            "name": "Wakooli Viola Ritah",
            "stack": "Python/FastAPI"
        },
        "timestamp": current_utc_time,
        "fact": cat_fact

    }
        

    return JSONResponse(content=profile_data, media_type="application/json")
