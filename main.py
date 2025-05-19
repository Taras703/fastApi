from fastapi import FastAPI, Query
from shemas import Person
from typing import List

app = FastAPI()

@app.get("/test1")
def read_item(parameter: List[str] = Query(["default1", "default=2"], max_length=10)):
     return parameter


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/{key}")
def read_item(key: int,):
     return {"value1": key}


@app.post("/person")
def read_root(person: Person):
    return person
