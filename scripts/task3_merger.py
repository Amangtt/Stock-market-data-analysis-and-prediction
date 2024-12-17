import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import os, sys
current_dir = os.getcwd()
target_dir = os.path.join(current_dir, 'Stock-market-data-analysis-and-prediction')

sys.path.insert(0, target_dir)
from scripts.Sentiment_analysis import sentiment_analysis

class merge:
    def load_datas(news,stock):
        news=pd.read_csv(news)
        stock=pd.read_csv(stock)
        return news,stock
    
    def combine(news,stocks,ticker):
       
        news['date']= pd.to_datetime(news['date'], errors='coerce')
        stocks['Date']= pd.to_datetime(stocks['Date'])
        news['date'] = news['date'].dt.date
        stocks['Date'] = stocks['Date'].dt.date
        aligned_data = pd.merge(news, stocks, left_on='date', right_on='Date', how='inner')
        filtered_data=aligned_data[aligned_data['stock'] == ticker]
        filtered_data.drop(columns=['date'], inplace=True)
        return filtered_data
    
    def call_sentiment_analysis(news,stocks,combine):
        merged_data= combine
        df= sentiment_analysis(merged_data)
        df['Date'] = pd.to_datetime(df['Date'])
        mean_scores = df.groupby(df['Date'].dt.date)['score'].mean()
        df['score'] = mean_scores.reindex(df['Date'].dt.date).values
        df['sentiment']= df['score'].apply(lambda score: 'Positive' if score >= 0.05 
            else ('Negative' if score <= -0.05 else 'Neutral'))
        result_df = df.drop_duplicates(subset='Date')
        p=['Date', 'Close', 'sentiment','score']
        return result_df
   
    def final(news,stocks,call_sentiment_analysis):
        df= call_sentiment_analysis
        df['Daily Return'] = df['Close'].pct_change() 
        p=['Date', 'Close', 'score','sentiment','Daily Return']
        return df[p]
    
