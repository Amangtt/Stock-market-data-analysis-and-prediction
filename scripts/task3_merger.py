import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import os, sys
current_dir = os.getcwd()
target_dir = os.path.join(current_dir, 'Stock-market-data-analysis-and-prediction')
d=pd.read_csv('./Data/raw_analyst_ratings.csv')
b=pd.read_csv('./Data/financial_news.csv')

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
        filtered_data.drop(columns=['date'], inplace=True)
        return filtered_data
    
    def merge(d,b):
        
        d_selected = d[['headline', 'date']]
    
        # Perform inner merge on 'headline'
        df_merged = pd.merge(b, d_selected, on='headline', how='inner')
        
        # Drop the 'url' column
        df_merged = df_merged.drop(columns='url', errors='ignore')  # Ignore errors if 'url' is not present
        
        # Save to CSV
        df_merged.to_csv('./Data/financial_newss.csv', index=False)

        
    def final(news,stocks,call_sentiment_analysis):
        df= call_sentiment_analysis
        df['Daily Return'] = df['Close'].pct_change() 
        p=['Date', 'Close', 'score','sentiment','Daily Return']
        return df[p]
    
merge.merge(d,b)
