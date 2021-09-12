from .headers import headers
import pandas as pd

class Data:
    def __init__(self, path="RU.txt", headers=headers):
        self.table = pd.read_csv(path, sep='\t', names=headers, index_col = False)
        self.table['population'] = self.table['population'].fillna(0)
        self.table['alternatenames'] = self.table['alternatenames'].fillna('')
        self.table['alternatenames'] = self.table['alternatenames'].apply(lambda x: x.split(',') if x != '' else [])
       

    def getById(self, id:int) -> dict:
        data = self.table[self.table['geonameid'] == id]

        if not data.shape[0]:
            return {}

        return data.iloc[0].to_dict()

    def getByRusName(self, rusName:str) -> dict:
        data = self.table[self.table['alternatenames'].apply(lambda x: True if rusName.lower() in [i.lower() for i in x] else False)]

        if not data.shape[0]:
            return {}

        return data[data['population'] == data['population'].max()].iloc[0].to_dict()

    def getByNameContains(self, name:str) -> dict:
        data = self.table[self.table['name'].str.lower().str.startswith(name.lower())]['name'].unique().tolist()
        return { 'name' : data } if data else {}
    
    def getByName(self, name:str):
        return self.table[self.table['name'] == name]

    def getPage(self, page:int, quantity:int):
        if page <= 0 or quantity <= 0:
            return {}

        start = (page - 1) * quantity
        end = (page * quantity)

        end = end if end <= self.table.shape[0] else self.table.shape[0]

        return {} if start >= end else self.table.iloc[start:end].T.to_dict()

    

    
        



