import geopandas as gpd
import pandas as pd
import folium

# Caminhos dos arquivos
shapefile_path = r"C:\Users\Usuario\Documents\rota\bairros\Delimitação_dos_Bairros_-_Dec._32.791_2020.shp"
shapefile_ldf = r"C:\Users\Usuario\Documents\rota\bairros-ldf\Bairros_Geral_LF.shp"
csv_path = r"C:\Users\Usuario\Documents\rota\bairros.csv"

# Carregar os dados e converter o CRS para WGS84 (EPSG:4326)
gdf_bairros_ldf = gpd.read_file(shapefile_ldf).to_crs(epsg=4326)
gdf_bairros_ldf = gdf_bairros_ldf.rename(columns={'NOME': 'nome_bairr'})
gdf_bairros_ldf.loc[gdf_bairros_ldf["nome_bairr"].str.lower().str.strip() == "centro", "nome_bairr"] = "Centro de Lauro"
gdf_bairros_ssa = gpd.read_file(shapefile_path).to_crs(epsg=4326)
gdf_bairros = pd.concat([gdf_bairros_ssa, gdf_bairros_ldf], ignore_index=True)
df_rotas = pd.read_csv(csv_path)

# Função para normalizar os nomes dos bairros
def normalizar_nome(nome):
    if pd.isna(nome):
        return ""
    return (
        nome.strip().lower()
        .replace("ã", "a").replace("á", "a").replace("â", "a")
        .replace("é", "e").replace("ê", "e").replace("í", "i")
        .replace("ó", "o").replace("ô", "o").replace("õ", "o")
        .replace("ú", "u").replace("ç", "c")
    )

# Normalizar os nomes para a junção correta
gdf_bairros["nome_bairr"] = gdf_bairros["nome_bairr"].apply(normalizar_nome)
df_rotas["bairros"] = df_rotas["bairros"].apply(normalizar_nome)

# Realizar a junção dos dados
gdf_bairros = gdf_bairros.merge(df_rotas, left_on="nome_bairr", right_on="bairros", how="left")

# Dicionário que mapeia cada número de rota para uma cor específica
color_map = {
    3: "blue",
    4: "green",
    5: "red",
    6: "purple",
    7: "orange",
    8: "beige",
    9: "pink"
}

# Função que retorna a função de estilo com a cor definida
def get_style_function(fillColor):
    return lambda feature: {
        "fillColor": fillColor,
        "color": "black",      # Borda preta
        "weight": 1,           # Espessura da borda
        "fillOpacity": 0.5     # Opacidade do preenchimento
    }

# Criar o mapa base (Salvador como centro)
m = folium.Map(location=[-12.9714, -38.5016], zoom_start=12, tiles="cartodb positron")

# Adicionar os polígonos dos bairros ao mapa
for idx, row in gdf_bairros.iterrows():
    # Obter o centroide para posicionar o marcador
    centroid = row["geometry"].centroid
    bairro_nome = row["nome_bairr"].title()
    rota = row["rota"]

    # Definir a cor de preenchimento de acordo com a rota
    if pd.notna(rota):
        try:
            # Converter para int (tratando casos como "3.0")
            rota_int = int(float(rota))
            fillColor = color_map.get(rota_int, "blue")
        except Exception:
            fillColor = "blue"
    else:
        fillColor = "lightgray"
    
    # Converter a geometria para dicionário GeoJSON e aplicar o estilo
    folium.GeoJson(
        row["geometry"].__geo_interface__,
        style_function=get_style_function(fillColor),
        tooltip=bairro_nome
    ).add_to(m)
    
    # Adicionar marcador com o nome do bairro (e rota, se existir)
    popup_text = f"{bairro_nome} - Rota: {rota}" if pd.notna(rota) else bairro_nome
    folium.Marker(
        [centroid.y, centroid.x],
        popup=popup_text,
        icon=folium.Icon(color="black", icon="info-sign")
    ).add_to(m)

# Salvar o mapa interativo como HTML
m.save("mapa.html")
m