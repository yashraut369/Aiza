from transformers import pipeline

nlp = pipeline("sentiment-analysis")

def analyze_sentiment(text):
    return nlp(text)