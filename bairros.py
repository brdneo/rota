import geopandas as gpd

shapefile_path = r"C:\Users\Usuario\Documents\rota\bairros\Delimitação_dos_Bairros_-_Dec._32.791_2020.shp"
gdf = gpd.read_file(shapefile_path)

print(gdf)
