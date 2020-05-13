def compare_trades(house_trades, street_trades):
    house_matched = [False for _ in range(len(house_trades))]
    street_matched = [False for _ in range(len(street_trades))]
    # step 1: get all the exact matched trade pairs
    for i in range(len(house_trades)):
        for j in range(len(street_trades)):
            if not street_matched[j] and exact_match(house_trades[i], street_trades[j]):
                house_matched[i] = True
                street_matched[j] = True
                # after we found a match, we need to stop matching and break
                break
    print('after exact match: {} \n {}'.format(house_matched, street_matched))

    # step 2: get all fuzzy matched trade pairs
    for i in range(len(house_trades)):
        if house_matched[i]:
            continue
        for j in range(len(street_trades)):
            if street_matched[j]:
                continue
            if fuzzy_match(house_trades[i], street_trades[j]):
                house_matched[i] = True
                street_matched[j] = True
                # after we found a match, we need to stop matching and break
                break

    print('after fuzzy match: {} \n {}'.format(house_matched, street_matched))

    # step 3: handle offset matching respectively within house_trades and street_trades
    house_trades_offset = []
    for i in range(len(house_trades)):
        if house_matched[i]:
            continue
        house_trades_offset.append(house_trades[i])
    house_trades_offset = filter_out_offset_match(house_trades_offset)
    print('after offset match, house_trades = {}'.format(house_trades_offset))

    street_trades_offset = []
    for j in range(len(street_trades)):
        if street_matched[j]:
            continue
        street_trades_offset.append(street_trades[j])
    street_trades_offset = filter_out_offset_match(street_trades_offset)
    print('after offset match, street_trades = {}'.format(street_trades_offset))

    # might need to sort the output but that should be easy
    return house_trades_offset + street_trades_offset


def exact_match(trade1, trade2):
    return trade1 == trade2


def fuzzy_match(trade1, trade2):
    def fuzz(x):
        return ','.join(x.split(',')[:3])
    return fuzz(trade1) == fuzz(trade2)


def offset_match(trade1, trade2):
    trade1_param = trade1.split(',')
    trade2_param = trade2.split(',')
    return trade1_param[0] == trade2_param[0] and trade1_param[2] == trade2_param[2]


def filter_out_offset_match(trades):
    matched = [False for _ in range(len(trades))]
    # split the trades into a buy list and a sell list
    buy_trades, sell_trades = [], []
    for i, trade in enumerate(trades):
        trade_param = trade.split(',')
        if trade_param[1] == 'B':
            buy_trades.append((i, trade))
        else:
            sell_trades.append((i, trade))

    # sort by the trade ID
    buy_trades.sort(key=lambda x: x[1].split(',')[3])
    sell_trades.sort(key=lambda x: x[1].split(',')[3])

    for i, buy_trade in buy_trades:
        for j, sell_trade in sell_trades:
            if not matched[j] and offset_match(buy_trade, sell_trade):
                matched[i] = True
                matched[j] = True
                break
    res = []
    for i in range(len(trades)):
        if not matched[i]:
            res.append(trades[i])

    return res


if __name__ == '__main__':
    house_trades = [
        "GOOG,S,0050,111111",
        "APPL,B,0010,ABC123",
        "APPL,S,0010,ZYX444",
        "GOOG,S,0050,000000",
        "GOOG,B,0050,333333",
        "GOOG,B,0050,222222",
    ]

    street_trades = [
        "GOOG,S,0050,GHG545",
        "APPL,S,0010,ZYX444",
        "APPL,B,0010,TTT222",
        "APPL,B,0010,000000",
        "APPL,S,0010,111111",
        "APPL,S,0010,111112",
    ]

    print compare_trades(house_trades, street_trades)
