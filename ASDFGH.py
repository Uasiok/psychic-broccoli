

from fastapi import FastAPI
import uvicorn
import random

app = FastAPI()
@app.get("/")
def help():
    return {"data" : "/hello - привет, /rng - случайное число"}
@app.get("/hello")
def hello():
    return {"data" : "Hello!"}
@app.get("/rng")
def rng(lower : int, upper : int):
    return {"data" : random.randint(lower,upper)}

if __name__ == "__main__":
    uvicorn.run("ASDFGH:app", host = "0.0.0.0", port = 8000)
