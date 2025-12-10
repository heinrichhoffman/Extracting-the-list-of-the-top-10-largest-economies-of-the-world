import requests
import pandas as pd
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29"

resp = requests.get(URL)
resp.raise_for_status()

soup = BeautifulSoup(resp.text, "html.parser")

# Localize a tabela que contém os dados de GDP nominal — geralmente a primeira ou a tabela com caption contendo "IMF"
table = soup.find("table", {"class": "wikitable"})

df = pd.read_html(str(table))[0]

# Supondo que a coluna de PIB nominal esteja marcada como e.g. "2025 IMF" ou similar — ajuste conforme necessário
# Filtrar apenas os 10 primeiros países
top10 = df.head(10)

# Converter PIB para float (US$ bilhões/trilhões conforme formato) e arredondar
# Dependendo do formato, pode haver processamento adicional

print(top10)
