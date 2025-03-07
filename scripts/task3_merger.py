import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import os, sys
current_dir = os.getcwd()
target_dir = os.path.join(current_dir, 'Stock-market-data-analysis-and-prediction')


sys.path.insert(0, target_dir)


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
        filtered_data = filtered_data.drop_duplicates(subset=['date'], keep='first')
        filtered_data.drop(columns=['date'], inplace=True)
        return filtered_data
    


        
    def final(call_sentiment_analysis):
        df= call_sentiment_analysis
        df['Close'] = pd.to_numeric(df['Close'], errors='coerce')
        df['Daily Return'] = df['Close'].pct_change() 
        df['Lagged Sentiment'] = df['score'].shift(1)
        p=['Date', 'Close', 'score','sentiment','Daily Return','Lagged Sentiment']
        return df[p]
    
    def compute_correlation(df):
        # Drop NaN values in 'Daily Return' for correlation analysis
        df = df.dropna(subset=['Daily Return'])

        # Compute Pearson correlation between sentiment score and stock return
        correlation = df[['Lagged Sentiment', 'Daily Return']].corr().iloc[0, 1]
        
        print(f"Correlation between sentiment score and stock movement: {correlation:.4f}")
        return correlation
