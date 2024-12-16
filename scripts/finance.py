import pandas as pd
import numpy as np
import plotly.express as px
import talib
import matplotlib.pyplot as plt
import pynance as pn


class financial_analysis:

    # Loading data
    def load_data(file):
        df= pd.read_csv(file)
        return df
    
    # Checking existance of the specified columns
    def check_existance(df):
        if all(col in df.columns for col in ['Open', 'Close','High', 'Low','Volume' ]):
            return True
        else:
            return False
        
    # Calculating techincal indicators    
    def calculate_technical_indicators(df):
        df['SMA'] = talib.SMA(df['Close'], timeperiod=10)  
        df['EMA'] = talib.EMA(df['Close'], timeperiod=10)  
        df['RSI'] = talib.RSI(df['Close'], timeperiod=10)
        macd,macd_signal,_= talib.MACD(df['Close'])
        df['MACD']=macd
        df['MACD_SIGNAL']= macd_signal
        df_cleaned = df.dropna(subset=['Close', 'SMA','RSI','MACD','MACD_SIGNAL'])
        
        return df_cleaned
    
    # plotting open,close,high and low columns           
    def OHLC(df):
        price_types = ['Open', 'Close', 'High', 'Low']
        df['Date'] = pd.to_datetime(df['Date'])

        # Extract the year from the 'date' column
        df['year'] = df['Date'].dt.year
        for i, p in enumerate(price_types):
            plt.subplot(2, 2, i + 1)  
            plt.plot(df['year'], df[p],  color='blue')
            plt.title(f"{p}")
            plt.xticks(rotation=45)
            plt.legend()
            plt.grid()
            plt.tight_layout()  # Adjust layout to prevent overlap
            plt.show()

        #ploting SMA,EMA and the others by accepting there name in the graph parameter 
    def plot_TI(df,graph):        
        plt.figure(figsize=(10, 5))
        plt.plot(df.index, df['Close'], label='Close', color='blue')
        plt.plot(df.index, df[graph], label=graph, color='orange')
        plt.show()
           
        
        # Financial Metrics
    def metrics(df):
        df['Date'] = pd.to_datetime(df['Date'])
        df['year'] = df['Date'].dt.year

        df['Daily Return'] = df['Close'].pct_change()
        df['Cumulative Return'] = (1 + df['Daily Return']).cumprod() - 1
        df['Volatility'] = df['Daily Return'].std() * np.sqrt(252) 
        plt.figure(figsize=(15, 10))

            # Plot Daily Return
        plt.subplot(3, 1, 1)
        plt.plot(df['Date'], df['Daily Return'], label='Daily Return', color='blue')
        plt.title('Daily Return')
        plt.ylabel('Return')
        plt.axhline(0, color='gray', linestyle='--')
        plt.legend()
        plt.grid()

        # Plot Cumulative Return
        plt.subplot(3, 1, 2)
        plt.plot(df['Date'], df['Cumulative Return'], label='Cumulative Return', color='green')
        plt.title('Cumulative Return')
        plt.ylabel('Cumulative Return')
        plt.axhline(0, color='gray', linestyle='--')
        plt.legend()
        plt.grid()

        # Display Volatility
        plt.subplot(3, 1, 3)
        plt.text(0.5, 0.5, f'Annualized Volatility: {df["Volatility"].iloc[-1]:.4f}', fontsize=15, ha='center')
        plt.axis('off')
        plt.title('Volatility')

        plt.tight_layout()
        plt.show()
        
    
    