import uuid
from datetime import datetime

from flask import Flask
from pydantic import BaseModel


class Trip(BaseModel):
    id: uuid.UUID
    name: str
    departure: datetime
    price: int  # in euro cents


app = Flask(__name__)


@app.get("/")
def list_trips():
    return {"trips": []}
