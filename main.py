import ai
import parse
from fastapi import FastAPI, UploadFile, File

app = FastAPI()
@app.post("/analyze")
@app.get("/")
async def analyze_resume(file: UploadFile = File(...)):

    contents = await file.read()
    text = parse.parse_pdf(contents)
    result_json = ai.ai_analyze(text)
    return result_json
    