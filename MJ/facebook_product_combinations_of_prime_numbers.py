# Given a list of prime numbers, return all possible products that could be generated
def product_combinations(nums):
    res = set()
    if not nums:
        return res
    dfs(nums, 0, 1, res)
    return res


def dfs(nums, start, cur, res):
    if start == len(nums):
        res.add(cur)
        return
    if cur > 1:
        res.add(cur)
    for i in range(start, len(nums)):
        dfs(nums, i+1, cur * nums[i], res)


if __name__ == '__main__':
    nums = [2,2,3,5]
    print product_combinations(nums)
