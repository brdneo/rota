import geopandas as gpd

shapefile_path = r"C:\Users\Usuario\Documents\rota\bairros\Delimitação_dos_Bairros_-_Dec._32.791_2020.shp"
gdf = gpd.read_file(shapefile_path)

#print(gdf)

shapefile_ldf = r"C:\Users\Usuario\Documents\rota\bairros-ldf\Bairros_Geral_LF.shp"
ldf = gpd.read_file(shapefile_ldf)
ldf = ldf.rename(columns={'NOME': 'nome_bairr'})
ldf.loc[ldf["nome_bairr"].str.lower().str.strip() == "centro", "nome_bairr"] = "Centro de Lauro"
#print(ldf)

interior = r"C:\Users\Usuario\Documents\rota\interior\interior.shp"
inte = gpd.read_file(interior)
inte = inte.rename(columns={'MUNICIPIO': 'nome_bairr'})
#print(inte)

feira = r"C:\Users\Usuario\Documents\rota\feira-santana\feira-de-santana.shp"
fds = gpd.read_file(feira)
fds = fds.rename(columns={'MUNICIPIO': 'nome_bairr'})
print(fds)