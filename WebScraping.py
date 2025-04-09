import requests
import pandas as pd

# 🔑 Substitua aqui pela sua chave real da API do CoinMarketCap
API_KEY = 'Coloque a sua Chave'

# 📡 Endpoint da API
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

# ⚙️ Parâmetros da requisição
parameters = {
    'start': '1',
    'limit': '100',
    'convert': 'USD'
}

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': API_KEY
}

# 🔄 Faz a requisição
response = requests.get(url, headers=headers, params=parameters)

if response.status_code == 200:
    data = response.json()
    crypto_data = []

    for crypto in data.get('data', []):
        name = crypto['name']
        volume_24h = crypto['quote']['USD']['volume_24h']

        if volume_24h > 50000:
            slug = crypto['slug']
            coin_url = f"https://coinmarketcap.com/currencies/{slug}/"
            email = "Indisponível"
            listed_on_biconomy = "Indisponível"

            crypto_data.append({
                'Nome': name,
                'E-mail': email,
                'Link CoinMarketCap': coin_url,
                'Volume (24h)': round(volume_24h, 2),
                'Listada na Biconomy': listed_on_biconomy
            })

    df = pd.DataFrame(crypto_data)
    df.to_excel('Scraping no CoinMarketCap.xlsx', index=False)
    print("✅ Excel gerado com sucesso!")

else:
    print(f"❌ Erro na requisição: {response.status_code}")
    print(response.text)
