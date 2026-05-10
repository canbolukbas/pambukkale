import uuid
from datetime import datetime

from flask import Flask

app = Flask(__name__)


@app.get("/")
def list_trips():
    trips = [
        {
            "id": uuid.uuid4(),
            "name": "",
            "departure": datetime.now(),
            "price": 0,
        }
    ]
    return {"trips": [trip for trip in trips]}
