import requests
import json
from config import keys

class CriptoConverter():
    @staticmethod
    def check_param(quote: str, base: str, amount: str):

        if quote == base:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}')


    @staticmethod
    def get_price(quote: str, base: str, amount: str):

        quote_ticker = keys[quote]
        base_ticker = keys[base]

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]
        return [total_base, float(amount)*float(total_base)]


class APIException(Exception):
    pass