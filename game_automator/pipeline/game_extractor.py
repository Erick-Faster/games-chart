from config import config
import pandas as pd
import numpy as np
import requests
import json

class GameExtractor(object):
    def __init__(self):
        self.token = config.TOKEN
        self.id_database = config.ID_DATABASE
        self.headers = config.HEADERS
        self.url = config.URL
        
    def extract_page(self, cursor = False):
        
        cursor_json = {}
        if cursor:
            cursor_json = {'start_cursor':cursor}
        
        results = requests.post(self.url, headers=self.headers, json=cursor_json)
        
        if results.status_code != 200:
            raise TypeError(f'Cannot import data. {results.json()}')

        data_raw = results.json()
        pag_data = {
            'has_more': data_raw['has_more'],
            'next_cursor': data_raw['next_cursor']}
                    
        data_list = data_raw['results']
        
        df_list = []
        for data in data_list:
            
            game = data['properties']['Game']['title'][0]['plain_text']
            status = data['properties']['Status']['select']['name']
            
            
            try:
                rating = data['properties']['Rating']['select']['name']
            except TypeError:
                rating = '0'
                
            try:
                finished = data['properties']['Finished']['date']['start']
            except TypeError:
                finished = np.nan    
        
            try:
                genre = data['properties']['Genre']['select']['name']
            except TypeError:
                genre = 'undefined'
        
            try:
                hours = data['properties']['Hours']['number']
            except TypeError:
                hours = np.nan
            
            temp_dict = {
                'game': game,
                'status': status,
                'rating': rating,
                'finished': finished,
                'genre': genre,
                'hours': hours}
            
            df_list.append(temp_dict)

        df = pd.DataFrame(df_list)
        return df, pag_data
    
    def extract_data(self):
        
        df_list = []

        df_temp, pag_data = self.extract_page()
        df_list.append(df_temp)
        
        has_more = pag_data['has_more']
        while has_more == True:
            next_cursor = pag_data['next_cursor']
            df_temp, pag_data = self.extract_page(cursor=next_cursor)
            df_list.append(df_temp)
            has_more = pag_data['has_more']
            
        df = pd.concat(df_list,axis=0)
        df = df.reset_index(drop=True)
        
        return df