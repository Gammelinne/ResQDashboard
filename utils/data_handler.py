import pandas as pd
from . import globals

class DataHandler:
    def __init__(self):
        self.filter = pd.read_csv(globals.PATH_CSV_FILTER)
        self.data = pd.read_csv(globals.PATH_CSV_DATA)

    def get_filter_data(self):
        # Return a dictionary with QIName as key, referenceDataColumns as value, and commentsInfo as comment
        qi_info = {}
        for _, row in self.filter.iterrows():
            # Vérifie si la colonne 'referenceDataColumns' existe dans le DataFrame
            if 'referenceDataColumns' in row.index:
                qi_info[row['QIName']] = {'referenceDataColumns': row['referenceDataColumns'], 'commentsInfo': row['commentsInfo']}
        return qi_info
    

    def get_data(self):
        #"site_country","site_name","site_id","discharge_year","discharge_quarter","YQ","subject_id","QI","Value","stroke_type","discharge_mrs","prenotification","imaging_done","three_m_mrs","gender","occup_physiotherapy_received","dysphagia_screening_done"
        return self.data