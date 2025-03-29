from os import getenv
import requests
from fastapi import HTTPException, status

ALPHAVANTAGE_APIKEY = getenv('ALPHAVANTAGE_APIKEY')

def sync_converter(from_currency: str, to_currency: str, price: float):
    url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={from_currency}&to_currency={to_currency}&apikey={ALPHAVANTAGE_APIKEY}'

    try:
        response = requests.get(url=url)
    except Exception as error:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    
    data = response.json()

    if 'Realtime Currency Exchange Rate' not in data:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Realtime Currency Exchange Rate not in response')
    
    exchange_rate = float(data['Realtime Currency Exchange Rate']['5. Exchange Rate'])

    return price * exchange_rate