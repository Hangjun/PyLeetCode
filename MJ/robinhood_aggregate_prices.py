from collections import defaultdict


def aggregate_prices(input):
    if not input:
        return []
    timestamps = [(int(item.split(':')[1]), int(item.split(':')[0])) for item in input.split(',')]
    ht = defaultdict(list)
    for ts in timestamps:
        ht[ts[0] / 10].append(ts)
    res = []
    last_interval = []
    max_interval = timestamps[-1][0]/10 + 1
    for i in range(max_interval):
        cur_interval = [i * 10]
        if i not in ht:
            if i == 0 or not last_interval:
                continue
            # use the last interval's data to populate this interval
            for _ in range(4):
                cur_interval.append(last_interval[2])
        else:
            interval_prices = [price for (ts, price) in ht[i]]
            first_price = interval_prices[0]
            last_price = interval_prices[-1]
            cur_interval.extend([first_price, last_price, max(interval_prices), min(interval_prices)])
        res.append(cur_interval)
        last_interval = cur_interval
    print res
    return res


if __name__ == '__main__':
    s1 = '1:0,3:10,2:12,4:19,5:35'
    s2 = '1:0,3:10,2:12,4:19,5:35,8:71,12:81,15:83,9:85'
    s3 = '8:71,12:81,15:83,9:85'
    s4 = ''
    aggregate_prices(s1)
    aggregate_prices(s2)
    aggregate_prices(s3)
    aggregate_prices(s4)
