from sklearn.base import BaseEstimator, TransformerMixin


# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.drop(labels=self.columns, axis='columns')

    
#fix some NA in the AVG Columns
class NanTrat1(BaseEstimator, TransformerMixin):
    def __init__(self, col1, col2, Target):
        self.col1 = col1
        self.col2 = col2
        self.Target = Target

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        # Primero copiamos el dataframe de datos de entrada 'X'
        data = X.copy()
        print(self.Target, " ", self.col1, " ", self.col2)
        # Devolvemos un nuevo dataframe de datos sin las columnas no deseadas
        data.loc[(data[self.Target].isna()) & ((data[self.col1] == 0) & (data[self.col2] == 0)), self.Target] = 0
        return data

    
