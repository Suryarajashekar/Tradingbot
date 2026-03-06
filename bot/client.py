import logging
from binance.client import Client
from config import API_KEY, API_SECRET, TESTNET_URL


class BinanceClient:

    def __init__(self):

        self.client = Client(API_KEY, API_SECRET)
        self.client.FUTURES_URL = TESTNET_URL

    def place_order(self, params):

        try:

            logging.info(f"Sending order request: {params}")

            order = self.client.futures_create_order(**params)

            logging.info(f"API response: {order}")

            return order

        except Exception as e:

            logging.error(f"API Error: {str(e)}")

            raise