import pandas as pd

class StatisticalAnalyzer:
    def __init__(self, df: pd.DataFrame):
        if not isinstance(df, pd.DataFrame):
            raise TypeError("Il dato deve essere un DataFrame pandas.")
        self.df = df.select_dtypes(include='number')  # Considera solo colonne numeriche

    def mean(self):
        return self.df.mean()

    def median(self):
        return self.df.median()

    def std_dev(self):
        return self.df.std()

    def variance(self):
        return self.df.var()

    def min_value(self):
        return self.df.min()

    def max_value(self):
        return self.df.max()

    def correlation(self):
        return self.df.corr()

    def covariance(self):
        return self.df.cov()

    def skewness(self):
        return self.df.skew()
    
    def kurtosis(self):
        return self.df.kurt()
    
    def quartiles(self):
        q1 = self.df.quantile(0.25)
        q2 = self.df.quantile(0.50)  # mediana
        q3 = self.df.quantile(0.75)
        return pd.DataFrame({'Q1': q1, 'Q2': q2, 'Q3': q3})
    
    def iqr(self):
        q1 = self.df.quantile(0.25)
        q3 = self.df.quantile(0.75)
        return q3 - q1
    
    def distribution_summary(self):
        return pd.DataFrame({
            'mean': self.mean(),
            'median': self.median(),
            'std_dev': self.std_dev(),
            'skewness': self.skewness(),
            'kurtosis': self.kurtosis(),
            'Q1': self.quartiles()['Q1'],
            'Q3': self.quartiles()['Q3'],
            'IQR': self.iqr()
        })

