import ai
import parse
from fastapi import FastAPI, UploadFile, File


app = FastAPI()
@app.post("/analyze")## having the thing run on POST http://127.0.0.1:8000/analyze
## analyzed the resume that we get using fast api
async def analyze_resume(file: UploadFile = File(...)):

    contents = await file.read()
    text = parse.parse_pdf(contents)
    result_json = ai.ai_analyze(text)
    return result_json
    