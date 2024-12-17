import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
from textblob import TextBlob
import matplotlib.pyplot as plt

sid=SentimentIntensityAnalyzer()

class news_:
    def load_data(file):
        df= pd.read_csv(file)
        return df

    def sentiment_analysis(df):
        # Extract headlines
        headlines = df['headline']
        
        # Apply sentiment analysis to each headline
        df['score'] = headlines.apply(lambda headline: TextBlob(headline).sentiment.polarity)
        
        # Classify sentiment based on polarity score
        df['sentiment'] = df['score'].apply(lambda score: 'Positive' if score >= 0.05 
                                            else ('Negative' if score <= -0.05 else 'Neutral'))
        
        return df

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

    # Function to count unique domains
    def count_unique_domains(df):
        domain_count = {}

        for publisher in df["publisher"]:
            if "@" in publisher:  # Checking if its an email
                domain = publisher.split("@")[-1]
                domain_count[domain] = domain_count.get(domain, 0) + 1

        return domain_count
    
    def plot_article_over_time(df):
    
        df['date']= pd.to_datetime(df['date'], errors='coerce')
        df['only date']= df['date'].dt.date
        count_by_date= df.groupby('only date').size().reset_index(name='Trend by date')
        plt.figure(figsize=(12, 6))
        plt.plot(count_by_date['only date'], count_by_date['Trend by date'], marker='o', linestyle='-', color='skyblue')
        plt.title('Number of Articles Published Over Time')
        plt.xlabel('Date')
        plt.ylabel('Number of Articles')
        plt.xticks(rotation=45)
        plt.grid(axis='y')
        plt.tight_layout()
        plt.show()

    def plot_article_by_hour(df):
        df['hour'] = df['date'].dt.hour
        hourly_counts = df['hour'].value_counts().sort_index()

        # Plotting the results
        plt.figure(figsize=(10, 5))
        hourly_counts.plot(kind='bar', color='skyblue')
        plt.xlabel('Hour')
        plt.ylabel('Number of Articles')
        plt.grid(axis='y')
        plt.show()
