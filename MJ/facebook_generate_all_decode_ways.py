def generate_all_decode_ways(s):
    if not s:
        return []
    if len(s) == 1:
        return [s] if validOne(s) else []
    res = []
    dfs("", s, res)
    return res


def dfs(prefix, remaining, res):
    n = len(remaining)
    if n == 0:
        res.append(prefix)
        return
    if not validOne(remaining[0]):
        return
    dfs(prefix + chr(int(remaining[0]) - 1 + ord('a')), remaining[1:], res)
    if n >= 2:
        if validTwo(remaining[0], remaining[1]):
            dfs(prefix + chr(int(remaining[0:2]) - 1 + ord('a')), remaining[2:], res)


def validOne(c):
    return ord('1') <= ord(c) <= ord('9')


def validTwo(a, b):
    return a == '1' or (a == '2' and ord('0') <= ord(b) <= ord('6'))


if __name__ == '__main__':
    s = '1123'
    print generate_all_decode_ways(s)

# Output: ['aabc', 'aaw', 'alc', 'kbc', 'kw']
