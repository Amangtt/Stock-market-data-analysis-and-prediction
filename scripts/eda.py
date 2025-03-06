import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
data=pd.read_csv('./Data/raw_analyst_ratings.csv')

class Descriptive:
    def __init__(self, data):
        self.df=data


    def des(self):
        self.df['headline length']=len(self.df['headline'])
        print(self.df)
    #des(data)
    def check_missing(self):
        
        print(self.df.isnull().sum())


    def no_article(self):
        publisher=self.df.groupby('publisher').size().reset_index(name='publisher count')
        publisher=publisher.sort_values(by='publisher count', ascending=False)
        print(publisher)
        
    def stock(self):
        df=self.df
        #df=df['date'].dropna()
        #df['date'] = pd.to_datetime(df['date'], format='mixed')
        df['date'] = df['date'].str[:10]
        df['date']= pd.to_datetime(df['date'])



        print(df.dtypes)
        """df[df['date'] > ]
        stocks=df.groupby('stock').size().reset_index(name='stock count')
        stocks=stocks.sort_values(by='stock count', ascending=False)
        print(stocks)"""

    def plot_article_over_time(self):
        df=self.df
        df['date'] = df['date'].str[:10]
        df['date'] = pd.to_datetime(df['date'])
        count_by_date= df.groupby('date').size().reset_index(name='Trend by date')
        plt.figure(figsize=(12, 6))
        plt.plot(count_by_date['date'], count_by_date['Trend by date'], marker='o', linestyle='-', color='skyblue')
        plt.title('Number of Articles Published Over Time')
        plt.xlabel('Date')
        plt.ylabel('Number of Articles')
        plt.xticks(rotation=45)
        plt.grid(axis='y')
        plt.tight_layout()
        plt.show()

call=Descriptive(data)

call.plot_article_over_time()