import numpy as np
import pandas as pd

class Analizer:
    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()
        if 'Date' in self.df.columns:
            self.df['Date'] = pd.to_datetime(self.df['Date']) # Convert to datetime
     
    # Analisi generali   
    def top_tracks(self, n=10):
        return self.df.nlargest(n, 'Streams') # Get top n tracks by streams
    
    def top_artists(self, n=10):
        return self.df.groupby('Artist')['Streams'].sum().nlargest(n)
    
    def most_streamed_track(self):
        idx = np.argmax(self.df['Streams'].values)
        return self.df.iloc[idx] # Get the most streamed track #iloc is used to get the row by index
    
    def streams_by_artist(self, artist):
        return self.df[self.df['Artist'].str.lower() == artist.lower()]# Get all tracks by a specific artist
    
    def tracks_above_threshold(self, threshold):
        return self.df[self.df['Streams'] > threshold]# Get all tracks with streams above a certain threshold
    
    def artists_track_count(self):
        return self.df.groupby('Artist')['Track'].count().reset_index(name='Track Count') # Count the number of tracks for each artist and return a DataFrame with the results
    
    # Analisi temporali per giorni
    def filter_by_day(self, day):
        if 'Date' in self.df.columns:
            raise ValueError("Date column not found in DataFrame")
        return self.df[self.df['Date'] >= pd.to_datetime(day)] # Filter tracks by a specific day
    
    def daily_streams_custom(self, day):
        df_filtered = self.filter_by_day(day)
        return df_filtered.groupby('Date')['Streams'].sum().reset_index() # Get daily streams for a specific day
    
    def top_artists_since(self, day, n=10):
        df_filtered = self.filter_by_day(day)
        return df_filtered.groupby('Artist')['Streams'].sum().nlargest(n) # Get top n artists since a specific day
    
    # Analisi temporali per mesi specifici
    def filter_by_month_range(self, start_month, end_month=None): # Filter tracks by one month or a range of months
        self.df['Month'] = self.df['Date'].dt.to_period('ME') # Create a new column with the month
        start = pd.Period(start_month, freq='ME')
        end = pd.Period(end_month, freq='ME')
        return self.df[(self.df['Month'] >= start) & (self.df['Month'] <= end)]
    
    def top_track_in_month(self, start_month, end_month=None):
        df_filtered = self.filter_by_month_range(start_month, end_month)
        idx =df_filtered.groupby('Month')['Streams'].idxmax() # Get the index of the max streams for each month
        return df_filtered.loc[idx].sort_values(by='Date') # Get the top track in each month and sort by date
    
    def top_artists_in_month(self, start_month, end_month=None, n=10):
        df_filtered = self.filter_by_month_range(start_month, end_month)
        return df_filtered.groupby('Artist')['Streams'].sum().nlargest(n) # Get the top n artists in a specific month or range of months
    
    def monthly_streams(self, start_month, end_month=None):
        df_filtered = self.filter_by_month_range(start_month, end_month)
        return df_filtered.groupby('Month')['Streams'].sum()# Get the monthly streams for a specific month or range of months

    
    
        