from colorama import Fore, init
from bot.client import BinanceClient
from bot.orders import create_order_params, execute_order
from bot.validators import *
from bot.loggingconfig import setup_logging

init()

def menu():

    print(Fore.CYAN + "\n=== Binance Futures Testnet Bot ===")

    symbol = input("Symbol (ex BTCUSDT): ").upper()
    side = input("Side (BUY/SELL): ").upper()
    order_type = input("Type (MARKET/LIMIT/STOP): ").upper()

    quantity = float(input("Quantity: "))

    price = None

    if order_type in ["LIMIT", "STOP"]:
        price = float(input("Price: "))

    return symbol, side, order_type, quantity, price


def main():

    setup_logging()

    try:

        symbol, side, order_type, quantity, price = menu()

        validate_symbol(symbol)
        validate_side(side)
        validate_order_type(order_type)
        validate_quantity(quantity)
        validate_price(order_type, price)

        client = BinanceClient()

        params = create_order_params(
            symbol,
            side,
            order_type,
            quantity,
            price
        )

        execute_order(client, params)

    except Exception as e:

        print(Fore.RED + f"Error: {str(e)}")


if __name__ == "__main__":
    main()