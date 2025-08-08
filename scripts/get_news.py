import requests
import json

# API de noticias gratuita para pruebas
url = "https://newsdata.io/api/1/news"
params = {
    "apikey": "pub_612fe264dddd4577b40750d6f7a24d44",  # Clave pública gratuita
    "language": "es",
    "country": "pe",
    "category": "top"
}

# Hacemos la solicitud a la API
response = requests.get(url, params=params)

# Revisamos si todo salió bien
if response.status_code == 200:
    data = response.json()
    
    # Guardamos los datos en un archivo JSON
    with open("data/raw/noticias.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print("✅ Noticias guardadas en 'noticias.json'")
else:
    print("❌ Error al obtener noticias:", response.status_code)

print("✅ Script ejecutado correctamente")