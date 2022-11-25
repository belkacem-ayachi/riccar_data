import pandas as pd
import json

meta_data = pd.read_excel('metadata.xls')
meta_data=meta_data.dropna().reset_index()

print(meta_data.columns)
print('data set head', meta_data.head())


with open('metadata.json','w') as f:
    json.dump(meta_data.to_dict(orient='records'),f, ensure_ascii=False)



