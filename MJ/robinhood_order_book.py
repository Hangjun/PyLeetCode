from heapq import heapify, heappush, heappop


def order_book(orders):
    # standing orders
    buy_heap = [] # max heap
    sell_heap = [] # min heap
    total_orders_executed = 0
    for order in orders:
        if order['side'] == 'buy':
            if not sell_heap:
                order['limit_price'] = -order['limit_price']
                heappush(buy_heap, order)
            else:
                # Try to buy as much as possible
                while order['quantity'] > 0 and sell_heap:
                    sell_order = heappop(sell_heap)
                    if sell_order['limit_price'] > order['limit_price']:
                        heappush(sell_heap, sell_order)
                        break
                    else:
                        unit_executed = min(sell_order['quantity'], order['quantity'])
                        total_orders_executed += unit_executed
                        sell_order['quantity'] -= unit_executed
                        order['quantity'] -= unit_executed
                        if sell_order['quantity'] > 0:
                            heappush(sell_heap, sell_order)
                if order['quantity'] > 0:
                    order['limit_price'] *= -1
                    heappush(buy_heap, order)
        elif order['side'] == 'sell':
            if not buy_heap:
                heappush(sell_heap, order)
            else:
                # Try to sell as much as possible
                while order['quantity'] > 0 and buy_heap:
                    buy_order = heappop(buy_heap)
                    buy_order['limit_price'] *= -1
                    if buy_order['limit_price'] < order['limit_price']:
                        buy_order['limit_price'] *= -1
                        heappush(buy_heap, buy_order)
                        break
                    else:
                        unit_executed = min(buy_order['quantity'], order['quantity'])
                        total_orders_executed += unit_executed
                        buy_order['quantity'] -= unit_executed
                        order['quantity'] -= unit_executed
                        if buy_order['quantity'] > 0:
                            buy_order['limit_price'] *= -1
                            heappush(buy_heap, buy_order)
                if order['quantity'] > 0:
                    heappush(sell_heap, order)
        else:
            raise RuntimeError('Unknown transaction type!')

    print('Executed {} orders in total'.format(total_orders_executed))
    return total_orders_executed


if __name__ == '__main__':
    orders = [
        {'limit_price': 150, 'quantity': 10, 'side': 'buy'},
        {'limit_price': 165, 'quantity': 7, 'side': 'sell'},
        {'limit_price': 168, 'quantity': 3, 'side': 'buy'},
        {'limit_price': 155, 'quantity': 5, 'side': 'sell'},
        {'limit_price': 166, 'quantity': 8, 'side': 'buy'},
        # {'limit_price': 170, 'quantity': 2, 'side': 'buy'},
        # {'limit_price': 110, 'quantity': 15, 'side': 'sell'},
    ]

    order_book(orders)
