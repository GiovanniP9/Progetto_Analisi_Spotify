import pandas as pd
from analisi import Analizer
from df import dataframe
from statistical_analysis import StatisticalAnalyzer
from visualization import Visualizer

def main():
    # Load data and initialize classes
    df = dataframe()
    analizer = Analizer(df)
    stat_analyzer = StatisticalAnalyzer(df.select_dtypes(include='number'))
    visualizer = Visualizer(analizer)
    
    # Main menu
    while True:
        print("\n" + "="*50)
        print("SPOTIFY DATA ANALYSIS MENU")
        print("="*50)
        print("\nMAIN CATEGORIES:")
        print("1. General Analysis")
        print("2. Temporal Analysis")
        print("3. Statistical Analysis")
        print("4. Visualizations")
        print("5. Exit")
        
        choice = input("\nSelect a category (1-5): ")
        
        if choice == "1":
            general_analysis_menu(analizer)
        elif choice == "2":
            temporal_analysis_menu(analizer)
        elif choice == "3":
            statistical_analysis_menu(stat_analyzer)
        elif choice == "4":
            visualizations_menu(visualizer)
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

def general_analysis_menu(analizer):
    while True:
        print("\n" + "-"*50)
        print("GENERAL ANALYSIS MENU")
        print("-"*50)
        print("1. Show top tracks")
        print("2. Show top artists")
        print("3. Show most streamed track")
        print("4. Show tracks by artist")
        print("5. Show tracks above stream threshold")
        print("6. Show artist track counts")
        
        
        choice = input("\nSelect an option (1-13): ")
        
        if choice == "1":
            n = int(input("How many tracks to show? (default 10): ") or 10)
            print(analizer.top_tracks(n))
        elif choice == "2":
            n = int(input("How many artists to show? (default 10): ") or 10)
            print(analizer.top_artists(n))
        elif choice == "3":
            print(analizer.most_streamed_track())
        elif choice == "4":
            artist = input("Enter artist name: ")
            print(analizer.streams_by_artist(artist))
        elif choice == "5":
            threshold = int(input("Enter stream threshold: "))
            print(analizer.tracks_above_threshold(threshold))
        elif choice == "6":
            print(analizer.artists_track_count())
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please try again.")

def temporal_analysis_menu(analizer):
    while True:
        print("\n" + "-"*50)
        print("TEMPORAL ANALYSIS MENU")
        print("-"*50)
        print("1. Filter by day")
        print("2. Daily streams since date")
        print("3. Top artists since date")
        print("4. Filter by month range")
        print("5. Top track in month/range")
        print("6. Top artists in month/range")
        print("7. Monthly streams")
        print("8. Back to main menu")
        
        choice = input("\nSelect an option (1-13): ")
        
        if choice == "1":
            day = input("Enter date (YYYY-MM-DD): ")
            print(analizer.filter_by_day(day))
        elif choice == "2":
            day = input("Enter start date (YYYY-MM-DD): ")
            print(analizer.daily_streams_custom(day))
        elif choice == "3":
            day = input("Enter start date (YYYY-MM-DD): ")
            n = int(input("How many artists to show? (default 10): ") or 10)
            print(analizer.top_artists_since(day, n))
        elif choice == "4":
            start = input("Enter start month (YYYY-MM): ")
            end = input("Enter end month (YYYY-MM, optional): ") or None
            print(analizer.filter_by_month_range(start, end))
        elif choice == "5":
            start = input("Enter start month (YYYY-MM): ")
            end = input("Enter end month (YYYY-MM, optional): ") or None
            print(analizer.top_track_in_month(start, end))
        elif choice == "6":
            start = input("Enter start month (YYYY-MM): ")
            end = input("Enter end month (YYYY-MM, optional): ") or None
            n = int(input("How many artists to show? (default 10): ") or 10)
            print(analizer.top_artists_in_month(start, end, n))
        elif choice == "7":
            start = input("Enter start month (YYYY-MM): ")
            end = input("Enter end month (YYYY-MM, optional): ") or None
            print(analizer.monthly_streams(start, end))
        elif choice == "8":
            break
        else:
            print("Invalid choice. Please try again.")

def statistical_analysis_menu(stat_analyzer):
    while True:
        print("\n" + "-"*50)
        print("STATISTICAL ANALYSIS MENU")
        print("-"*50)
        print("1. Mean")
        print("2. Median")
        print("3. Standard deviation")
        print("4. Variance")
        print("5. Minimum value")
        print("6. Maximum value")
        print("7. Correlation")
        print("8. Covariance")
        print("9. Skewness")
        print("10. Kurtosis")
        print("11. Quartiles")
        print("12. Interquartile range (IQR)")
        print("13. Distribution summary")
        print("14. Back to main menu")
        
        choice = input("\nSelect an option (1-14): ")
        
        if choice == "1":
            print(stat_analyzer.mean())
        elif choice == "2":
            print(stat_analyzer.median())
        elif choice == "3":
            print(stat_analyzer.std_dev())
        elif choice == "4":
            print(stat_analyzer.variance())
        elif choice == "5":
            print(stat_analyzer.min_value())
        elif choice == "6":
            print(stat_analyzer.max_value())
        elif choice == "7":
            print(stat_analyzer.correlation())
        elif choice == "8":
            print(stat_analyzer.covariance())
        elif choice == "9":
            print(stat_analyzer.skewness())
        elif choice == "10":
            print(stat_analyzer.kurtosis())
        elif choice == "11":
            print(stat_analyzer.quartiles())
        elif choice == "12":
            print(stat_analyzer.iqr())
        elif choice == "13":
            print(stat_analyzer.distribution_summary())
        elif choice == "14":
            break
        else:
            print("Invalid choice. Please try again.")

def visualizations_menu(visualizer):
    while True:
        print("\n" + "-"*50)
        print("VISUALIZATIONS MENU")
        print("-"*50)
        print("1. Visualize top tracks")
        print("2. Visualize top artists")
        print("3. Visualize most streamed track")
        print("4. Visualize artist streams")
        print("5. Visualize tracks above threshold")
        print("6. Visualize artist track counts")
        print("7. Visualize daily streams")
        print("8. Visualize top artists since date")
        print("9. Visualize monthly streams")
        print("10. Visualize top tracks by month")
        print("11. Visualize top artists by month")
        print("12. Visualize position vs streams")
        print("13. Visualize streams pie chart")
        print("14. Show all visualizations")
        print("15. Back to main menu")
        
        choice = input("\nSelect an option (1-15): ")
        
        if choice == "1":
            n = int(input("How many tracks to visualize? (default 10): ") or 10)
            visualizer.visualize_top_tracks(n)
        elif choice == "2":
            n = int(input("How many artists to visualize? (default 10): ") or 10)
            visualizer.visualize_top_artists(n)
        elif choice == "3":
            visualizer.visualize_most_streamed_track()
        elif choice == "4":
            artist = input("Enter artist name: ")
            visualizer.visualize_streams_by_artist(artist)
        elif choice == "5":
            threshold = int(input("Enter stream threshold: "))
            visualizer.visualize_tracks_above_threshold(threshold)
        elif choice == "6":
            n = int(input("Show top how many artists? (default 15): ") or 15)
            visualizer.visualize_artists_track_count(n)
        elif choice == "7":
            day = input("Enter start date (YYYY-MM-DD): ")
            days = int(input("How many days to show? (default 30): ") or 30)
            visualizer.visualize_daily_streams(day, days)
        elif choice == "8":
            day = input("Enter start date (YYYY-MM-DD): ")
            n = int(input("How many artists to show? (default 10): ") or 10)
            visualizer.visualize_top_artists_since(day, n)
        elif choice == "9":
            start = input("Enter start month (YYYY-MM): ")
            end = input("Enter end month (YYYY-MM, optional): ") or None
            visualizer.visualize_monthly_streams(start, end)
        elif choice == "10":
            start = input("Enter start month (YYYY-MM): ")
            end = input("Enter end month (YYYY-MM, optional): ") or None
            visualizer.visualize_top_track_in_month(start, end)
        elif choice == "11":
            start = input("Enter start month (YYYY-MM): ")
            end = input("Enter end month (YYYY-MM, optional): ") or None
            n = int(input("How many artists to show? (default 10): ") or 10)
            visualizer.visualize_top_artists_in_month(start, end, n)
        elif choice == "12":
            visualizer.visualize_position_vs_streams()
        elif choice == "13":
            n = int(input("Show top how many artists? (default 7): ") or 7)
            visualizer.visualize_streams_pie_chart(n)
        elif choice == "14":
            visualizer.visualize_all()
        elif choice == "15":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()