# Projeto de Mapeamento de Bairros com Rotas

Este projeto integra dados geoespaciais e informações de rotas para gerar um mapa interativo dos bairros de Salvador e Lauro de Freitas. Usando Python, GeoPandas e Folium, o mapa exibe os bairros coloridos conforme a rota definida em um arquivo CSV, possibilitando uma visualização prática e informativa.

## Funcionalidades

-   **Leitura e Processamento de Dados Geográficos:**  
    Carregamento e conversão dos shapefiles de Salvador e Lauro de Freitas para o sistema de coordenadas WGS84 (EPSG:4326).

-   **Normalização e Junção de Dados:**  
    Padronização dos nomes dos bairros para facilitar a junção com os dados de rotas presentes em um CSV.

-   **Mapeamento de Cores:**  
    Atribuição de cores específicas aos bairros com base no número de rota definido, utilizando um dicionário de cores (color_map).

-   **Correção de Nomes de Bairros:**  
    Ajuste nos nomes de bairros para evitar duplicidade (por exemplo, renomeando o "Centro" de Lauro de Freitas para "centro de lauro de freitas").

-   **Visualização Interativa:**  
    Geração de um mapa interativo com Folium, exibindo tooltips e popups com informações sobre o bairro e sua rota, além de marcadores posicionados nos centroides dos polígonos.

## Estrutura do Projeto

├── README.md # Este arquivo ├── script.py # Código principal do projeto ├── data/ │ ├── bairros/ # Shapefile dos bairros de Salvador │ │ └── Delimitação*dos_Bairros*-\_Dec.\_32.791_2020.shp │ ├── bairros-ldf/ # Shapefile dos bairros de Lauro de Freitas │ │ └── Bairros_Geral_LF.shp │ └── bairros.csv # Arquivo CSV com informações de rotas └── mapa.html # Mapa interativo gerado

## Dependências

-   Python 3.x
-   [GeoPandas](https://geopandas.org/)
-   [Pandas](https://pandas.pydata.org/)
-   [Folium](https://python-visualization.github.io/folium/)

## Como Executar

1. **Instale as dependências:**

    ```bash
    pip install geopandas pandas folium
    ```

2. **Ajuste os caminhos dos arquivos:**  
   Certifique-se de que os caminhos para os shapefiles e o CSV estejam corretos no script.

3. **Execute o script:**

    ```bash
    python script.py
    ```

4. **Visualize o mapa:**  
   Abra o arquivo `mapa.html` em seu navegador para explorar o mapa interativo.

## Customizações e Considerações

-   **Paleta de Cores:**  
    O mapeamento de cores é definido pelo dicionário `color_map`. Você pode alterar as cores conforme sua preferência ou adicionar novas rotas com cores diferentes.

-   **Normalização de Nomes:**  
    A função `normalizar_nome` garante que os nomes dos bairros sejam padronizados antes da junção dos dados. Se os nomes em seus arquivos tiverem variações, ajuste essa função conforme necessário.

-   **Renomeação Específica de Bairros:**  
    Se houver bairros com nomes iguais em cidades diferentes (por exemplo, "Centro"), você pode renomear os registros de forma diferenciada para evitar conflitos. No exemplo, o bairro "Centro" de Lauro de Freitas é renomeado para "centro de lauro de freitas".

## Conclusão

Este projeto demonstra como integrar e visualizar dados geoespaciais com informações adicionais, facilitando a análise e a visualização interativa dos bairros e suas respectivas rotas. Contribuições, sugestões e melhorias são bem-vindas!
