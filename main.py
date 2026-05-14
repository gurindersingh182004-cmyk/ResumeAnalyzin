import ai
from fastapi import FastAPI, UploadFile, File

app = FastAPI()
@app.post("/analyze")
@app.get("/")
async def read_main():
    return {"msg": "Hello World"}