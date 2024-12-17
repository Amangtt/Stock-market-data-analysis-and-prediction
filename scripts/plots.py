import matplotlib.pyplot as plt
import pandas as pd

#df= pd.read_csv('C:/Users/hello/Desktop/Data/raw_analyst_ratings.csv/raw_analyst_ratings.csv')
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
