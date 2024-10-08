from Utilities import heatmap_generation


correlator_type = {
    "pr": "pearson",
    "sp": "spearman",
    "kd": "kendal"
}


class Correlator:
    def __init__(self,df,corr_type):
        self.columns = df.columns# denomino le colonne del dataframe
        self.corr_type = correlator_type[corr_type] + "correlation" # hetmap con colore di correlazione
        self.correlation = df.corr(method=correlator_type[corr_type])# correlazione

    def correlation_heatmap(self):
        heatmap_generator(self.correlation, self.columns)