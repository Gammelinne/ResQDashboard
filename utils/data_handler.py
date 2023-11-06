import pandas as pd
from . import globals

class DataHandler:
    def __init__(self):
        self.load_data()

    def load_data(self):
        # Load data using pandas from the specified CSV file
        self.df = pd.read_csv(globals.PATH_CSV)

    def get_data(self):
        # Return the loaded DataFrame
        return self.df
