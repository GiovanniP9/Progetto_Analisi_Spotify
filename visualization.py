import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from analisi import Analizer

class Visualizazion(Analizer):
    def __init__(self, df):
        super().__init__(df)
        
    
    def view_top_artists(self):
        res = self.top_artists() # Chiama il metodo top_artists() della classe padre
        
        plt.figure(figsize=(10, 6))
        sns.barplot(x=res['Artist'], y=res['Streams'])
        plt.title("Top Artists")
        plt.xlabel("Artista")
        plt.ylabel("Streams")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
        
    def view_top_tracks(self):
        res = self.top_tracks()
        
        plt.figure(figsize=(10, 6))
        sns.barplot(x=res['Track'], y=res['Streams'])
        plt.title("Top Tracks")
        plt.xlabel("Traccia")
        plt.ylabel("Streams")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
        
    def view_streams_by_artist(self):
        res = self.streams_by_artist()
        
        plt.figure(figsize=(10, 6))
        sns.barplot(x=res['Artist'], y=res['Streams'])
        plt.title("Streams per Artist")
        plt.xlabel("Artista")
        plt.ylabel("Streams")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
        
        

    
    
            