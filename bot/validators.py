VALID_SIDES = ["BUY", "SELL"]
VALID_TYPES = ["MARKET", "LIMIT", "STOP"]

def validate_symbol(symbol):

    if len(symbol) < 5:
        raise ValueError("Invalid symbol format")

def validate_side(side):

    if side not in VALID_SIDES:
        raise ValueError("Side must be BUY or SELL")

def validate_order_type(order_type):

    if order_type not in VALID_TYPES:
        raise ValueError("Order type must be MARKET / LIMIT / STOP")

def validate_quantity(quantity):

    if quantity <= 0:
        raise ValueError("Quantity must be positive")

def validate_price(order_type, price):

    if order_type in ["LIMIT", "STOP"] and price is None:
        raise ValueError("Price required for LIMIT/STOP orders")