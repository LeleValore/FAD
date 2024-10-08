import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler, MaxAbsScaler, RobustScaler

# Dizionario contenente le classi di normalizzazione in Python
normalizetors = {
    "ss": ("StandardScaler", StandardScaler),
    "mm": ("MinMaxScaler", MinMaxScaler),
    "ma": ("MaxAbsScaler", MaxAbsScaler),
    "rs": ("RobustScaler", RobustScaler),
}

# Definizione della classe
class Normalizator:
    def __init__(self, model, df, quantile_range=None):
        if model not in normalizetors:
            raise KeyError(f"Il modello '{model}' non è presente nel dizionario. Scegli tra: {list(normalizetors.keys())}")

        norm_tuple = normalizetors[model]
        self.normalization_name = norm_tuple[0]
        self.normalizator_obj = self.set_normalization_obj(quantile_range, norm_tuple)
        self.data = self.data_normalization(df)

    def set_normalization_obj(self, quantile_range, norm_tuple):
        # Se il normalizzatore scelto è RobustScaler e `quantile_range` è definito, passalo al costruttore
        if norm_tuple[0] == "RobustScaler" and quantile_range:
            return norm_tuple[1](quantile_range=quantile_range)
        # Per gli altri normalizzatori usa il costruttore di default
        return norm_tuple[1]()  

    def data_normalization(self, df):
        data_normalizate = pd.DataFrame(
            self.normalizator_obj.fit_transform(df.values)  # Normalizzazione dei dati e conversione in DataFrame
        )
        data_normalizate.columns = df.columns  # Riassegno le colonne originali
        return data_normalizate

    def __repr__(self):
        return f"Normalizator(model={self.normalization_name})"
