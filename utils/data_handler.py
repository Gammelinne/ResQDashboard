import pandas as pd
from . import globals

class DataHandler:
    def __init__(self):
        self.filter = pd.read_csv(globals.PATH_CSV_FILTER)
        self.data = pd.read_csv(globals.PATH_CSV_DATA)

    def get_filter_data(self):
        # Return a dictionary with QIName as key, referenceDataColumns as value, and commentsInfo as comment
        qi_info = {}
        check_unique_column = set()  # Utiliser un ensemble pour garantir l'unicité des colonnes
        for _, row in self.filter.iterrows():
            # Vérifie si la colonne 'referenceDataColumns' existe dans le DataFrame
            if 'referenceDataColumns' in row.index and pd.notna(row['referenceDataColumns']):
                reference_column = row['referenceDataColumns']
                if reference_column not in check_unique_column:
                    qi_name = row['QIName']
                    qi_info[qi_name] = {'referenceDataColumns': reference_column, 'commentsInfo': row['commentsInfo']}
                    check_unique_column.add(reference_column)
        return qi_info    

    def get_data(self):
        return self.data