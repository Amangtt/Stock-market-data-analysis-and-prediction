import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

sid=SentimentIntensityAnalyzer()


def con(df):
    # Count the occurrences of each publisher
    count = df.groupby('publisher').size().reset_index(name='publisher count')
    count = count.sort_values(by='publisher count', ascending=False)
    
    # Get the top 3 publishers
    top_3 = count.head(3)

    # Filter the original DataFrame for the top 3 publishers
    top_publishers = top_3['publisher'].tolist()
    filtered_df = df[df['publisher'].isin(top_publishers)]

    # Calculate sentiment scores for the headlines
    filtered_df['score'] = filtered_df['headline'].apply(lambda headline: sid.polarity_scores(headline)['compound'])

    # Classify sentiment based on compound score
    filtered_df['sentiment'] = filtered_df['score'].apply(lambda score: 'Positive' if score >= 0.05 
    else ('Negative' if score <= -0.05 else 'Neutral'))

    sentiment_counts_per_publisher = filtered_df.groupby('publisher')['sentiment'].value_counts().unstack(fill_value=0)
    return sentiment_counts_per_publisher



