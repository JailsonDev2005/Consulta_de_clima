import requests

cidade = input("Digite o nome da cidade: ")

# 1. Procurar a cidade
url_cidade = "https://geocoding-api.open-meteo.com/v1/search"

parametros_cidade = {
    "name": cidade,
    "count": 1,
    "language": "pt",
    "format": "json"
}

resposta = requests.get(url_cidade, params=parametros_cidade)
dados_cidade = resposta.json()

# 2. Verificar se encontrou a cidade
if "results" not in dados_cidade:
    print("Cidade não encontrada!")
else:
    latitude = dados_cidade["results"][0]["latitude"]
    longitude = dados_cidade["results"][0]["longitude"]
    nome = dados_cidade["results"][0]["name"]

    # 3. Consultar o clima
    url_clima = "https://api.open-meteo.com/v1/forecast"

    parametros_clima = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m"
    }

    resposta = requests.get(url_clima, params=parametros_clima)
    clima = resposta.json()

    temperatura = clima["current"]["temperature_2m"]
    umidade = clima["current"]["relative_humidity_2m"]
    vento = clima["current"]["wind_speed_10m"]

    print("\n--- Clima ---")
    print(f"Cidade: {nome}")
    print(f"Temperatura: {temperatura}°C")
    print(f"Umidade: {umidade}%")
    print(f"Vento: {vento} km/h")