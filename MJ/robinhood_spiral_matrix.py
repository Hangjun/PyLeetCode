def spiral_matrix(nums):
    if not nums:
        return []
    m, n = len(nums), len(nums[0])
    res = [0 for _ in range(m*n)]
    u, d, l, r = 0, m-1, 0, n-1
    k = 0
    while True:
        # top row
        for col in range(l, r+1):
            res[k] = nums[u][col]
            k += 1
        u += 1
        if u > d:
            break

        # right col
        for row in range(u, d+1):
            res[k] = nums[row][r]
            k += 1
        r -= 1
        if r < l:
            break

        # bottom row
        for col in range(r, l-1, -1):
            res[k] = nums[d][col]
            k += 1
        d -= 1
        if d < u:
            break

        # left col
        for row in range(d, u-1, -1):
            res[k] = nums[row][l]
            k += 1
        l += 1
        if l > r:
            break
    return res


if __name__ == '__main__':
    nums = [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]
    ]

    print spiral_matrix(nums)
