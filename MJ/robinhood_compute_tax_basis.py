from collections import deque, defaultdict


def compute_tax_basis(transactions):
    # dictionary of symbol: standing buy orders
    standing_buy_orders = defaultdict(deque)
    capital_gains = []
    for transaction in transactions:
        if transaction["side"] == "buy":
            standing_buy_orders[transaction["symbol"]].append(transaction)
        else:
            total_sell_count = transaction["quantity"]
            buy_queue = standing_buy_orders[transaction["symbol"]]
            # FIFO access the deque to compute the capital gains until we sell all the quantities
            while total_sell_count > 0:
                if not buy_queue:
                    raise RuntimeError('You cannot sell more than you buy!')
                earliest_buy = buy_queue[0]
                if earliest_buy["quantity"] <= total_sell_count:
                    amount_sold = earliest_buy["quantity"]
                    buy_queue.popleft()
                else:
                    amount_sold = total_sell_count
                    buy_queue[0]["quantity"] -= amount_sold
                total_sell_count -= amount_sold
                capital_gains.append(
                    {
                        "symbol": transaction["symbol"],
                        "quantity": amount_sold,
                        "capital_gain": (transaction["price"] - earliest_buy["price"]) * amount_sold
                    }
                )
    return capital_gains


transactions = [
    {'symbol': 'FB', 'side': 'buy', 'quantity': 1, 'price': 200.00},
    {'symbol': 'APPLE', 'side': 'buy', 'quantity': 2, 'price': 100.00},
    {'symbol': 'FB', 'side': 'sell', 'quantity': 1, 'price': 150.00},
    {'symbol': 'APPLE', 'side': 'buy', 'quantity': 1, 'price': 150.00},
    {'symbol': 'APPLE', 'side': 'sell', 'quantity': 1, 'price': 200.00},
    {'symbol': 'APPLE', 'side': 'buy', 'quantity': 4, 'price': 210.00},
    {'symbol': 'APPLE', 'side': 'sell', 'quantity': 4, 'price': 220.00},
]

capital_gains = compute_tax_basis(transactions)
for capital_gain in capital_gains:
    print capital_gain
