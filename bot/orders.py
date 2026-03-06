import logging

def create_order_params(symbol, side, order_type, quantity, price=None):

    params = {
        "symbol": symbol,
        "side": side,
        "type": order_type,
        "quantity": quantity
    }

    if order_type == "LIMIT":

        params["price"] = price
        params["timeInForce"] = "GTC"

    if order_type == "STOP":

        params["stopPrice"] = price
        params["type"] = "STOP_MARKET"

    return params


def execute_order(client, params):

    try:

        response = client.place_order(params)

        print("\nOrder Response")
        print("-----------------------")
        print("Order ID:", response.get("orderId"))
        print("Status:", response.get("status"))
        print("Executed Qty:", response.get("executedQty"))

        avg_price = response.get("avgPrice")

        if avg_price:
            print("Average Price:", avg_price)

        print("\nOrder successful")

        return response

    except Exception as e:

        logging.error(str(e))
        print("Order failed:", str(e))