import os
from binance.client import Client
from dotenv import load_dotenv

TESTNET_BASE_URL = "https://testnet.binancefuture.com"

def get_binance_client() -> Client:
    load_dotenv()

    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")

    if not api_key or not api_secret:
        raise ValueError("API key or secret not found in environment variables")

    client = Client(api_key, api_secret)
    client.FUTURES_URL = TESTNET_BASE_URL

    return client
