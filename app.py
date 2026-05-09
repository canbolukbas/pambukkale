from flask import Flask

app = Flask(__name__)


@app.get("/")
def list_trips():
    return {"trips": []}
