from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def fsfsfsfsfsd():
    return {"message": "Hello World"}
