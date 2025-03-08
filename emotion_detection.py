# Ensure sentiment_analysis.py exists or handle the import error
try:
    import sentiment_analysis
except ImportError:
    sentiment_analysis = None

def detect_emotion(text):
    if sentiment_analysis:
        return sentiment_analysis.analyze(text)
    else:
        return "Sentiment analysis module not found"