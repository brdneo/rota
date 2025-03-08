import json
import pandas as pd

df_shapefile = pd.read_csv("bairros_shapefile.csv", encoding="utf-8")

bairros_shapefile = set(df_shapefile["Bairro"].str.strip())

with open("bairros.json", "r", encoding="utf-8") as f:
    dados_json = json.load(f)
    
bairros_json = set(bairro["nome"].strip() for bairro in dados_json["bairros"])

bairros_exclusivos_shapefile = bairros_shapefile - bairros_json
print(bairros_exclusivos_shapefile)

bairros_exclusivos_json = bairros_json - bairros_shapefile
print(bairros_exclusivos_json)
