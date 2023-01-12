from fastapi import FastAPI, Form, Request
from transformers import pipeline

# Create an instance of the FastAPI web framework
app = FastAPI()

# Define the model name to be used for sentiment analysis
MODEL_NAME = "siebert/sentiment-roberta-large-english"

# Create a pipeline object for sentiment analysis using the defined model
sentiment_analysis = pipeline("sentiment-analysis", model=MODEL_NAME)

# Define a route for the root URL
@app.get("/")
def read_root():
    # Return a simple greeting when the root URL is accessed
    return {"Hello": "World"}


# Define a route for the /analyze endpoint
@app.post("/analyze")
async def analyze(request: Request, text: str = Form(...)):
    # Use the sentiment_analysis pipeline to analyze the sentiment of the passed text
    # and return the result as a JSON object
    return {"sentiment": sentiment_analysis(text)}
