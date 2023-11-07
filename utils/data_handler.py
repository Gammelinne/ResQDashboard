import pandas as pd
from . import globals

class DataHandler:
    def __init__(self):
        self.df = pd.read_csv(globals.PATH_CSV)

    def get_data(self):
        # Return the loaded DataFrame
        return self.df

    def get_qi_data(self):
        # Return a dictionary with QIName as key, referenceDataColumns as value, and commentsInfo as comment
        qi_info = {}
        for _, row in self.df.iterrows():
            # Vérifie si la colonne 'referenceDataColumns' existe dans le DataFrame
            if 'referenceDataColumns' in row.index:
                qi_info[row['QIName']] = {'referenceDataColumns': row['referenceDataColumns'], 'commentsInfo': row['commentsInfo']}
        return qi_info