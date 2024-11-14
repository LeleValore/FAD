from itertools import combinations
from sklearn.covariance import EmpiricalCovariance
from Utilities import heatmap_generation

class Covarianzer:
    def __init__(self, df):
        self.cols = list(df.columns)  # Prendi i nomi delle colonne del dataframe
        self.covariance_matrix = self.covariance_computing(df)  # Chiama il metodo interno per calcolare la matrice di covarianza

    def covariance_computing(self, df):
        """Calcola la matrice di covarianza usando EmpiricalCovariance di sklearn."""
        cov = EmpiricalCovariance(assume_centered=True).fit(df.values)  # Fit del modello sui dati
        return cov

    def cov_heatmap(self):
        """Genera una heatmap della matrice di covarianza usando la funzione heatmap_generation."""
        heatmap_generation(
            self.covariance_matrix.covariance_,  # Matrice di covarianza
            self.cols  # Nomi delle colonne
        )
