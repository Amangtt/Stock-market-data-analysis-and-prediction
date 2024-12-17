from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
import pandas as pd

# Initialize VADER sentiment analyzer
sid = SentimentIntensityAnalyzer()

def sentiment_analysis(df):
    headline= df['headline']
    # Apply sentiment analysis to each headline
    # lambda is an anounumous function 
    df['score'] = df['headline'].apply(lambda headline: sid.polarity_scores(headline)['compound'])
    # Classify sentiment based on compound score
    df['sentiment'] = df['score'].apply(lambda score: 'Positive' if score >= 0.05 
            else ('Negative' if score <= -0.05 else 'Neutral'))
    return df

