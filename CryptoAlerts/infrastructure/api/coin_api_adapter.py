import requests
from application.interfaces.api_interface import ApiInterface
from application.errors.crypto_errors import ApiError

class CoinApiAdapter(ApiInterface):
    def __init__(self, api_key):
        self.api_key = api_key
        self.headers = {
            'X-CoinAPI-Key': self.api_key
        }

    def get_current_value(self, crypto, devise):
        try:
            response = requests.get(f'https://rest.coinapi.io/v1/exchangerate/{crypto}/{devise}', headers=self.headers)
            data = response.json()
            if 'rate' in data:
                return data['rate']
        except requests.exceptions.RequestException as e:
            raise ApiError(f"Erreur lors de l'envoi de la requête à l'API : {e}")
        return None

    def is_valid_crypto(self, crypto):
        valid_cryptos = ['BTC', 'ETH', 'XRP', 'LTC', 'BCH', 'BNB', 'USDT', 'EOS', 'BSV', 'XLM', 'ADA', 'DOT', 'UNI', 'USDC', 'DOGE']
        return crypto.isupper() and crypto in valid_cryptos

    def is_valid_currency(self, devise):
        valid_currencies = ['USD', 'EUR', 'GBP', 'JPY', 'AUD', 'CAD', 'CHF', 'CNY', 'SEK', 'NZD']
        return devise.isupper() and devise in valid_currencies
