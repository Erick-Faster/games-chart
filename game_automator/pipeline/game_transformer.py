import pandas as pd

class GameTransformer(object):
    def __init__(self):
        pass

    def transform_data(self, df):
        df['hours'] = df['hours'].astype('Int64')
        return df