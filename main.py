from fastapi import FastAPI, Form, Request
from transformers import pipeline


app = FastAPI()
MODEL_NAME = "siebert/sentiment-roberta-large-english"


sentiment_analysis = pipeline("sentiment-analysis",model=MODEL_NAME)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/analyze")
async def analyze(request: Request, text: str = Form(...)):
    return {"sentiment": sentiment_analysis(text)
}