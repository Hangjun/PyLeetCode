def sparse_vector_product(A, B):
    if len(A) != len(B):
        return None
    # process A and B to extract non-zero (index, value) pairs
    A_reduced = []
    for i, a in enumerate(A):
        if a:
            A_reduced.append((i, a))
    B_reduced = []
    for i, b in enumerate(B):
        if b:
            B_reduced.append((i, b))

    product = 0
    # traverse A_reduced and binary search in B_reduced to find corresponding (index, value) pair
    for i, a in A_reduced:
        j = binary_search(B_reduced, i)
        if j != -1:
            product += a * B_reduced[j][1]
    return product


def binary_search(nums, index):
    left, right = 0, len(nums)-1
    while left <= right:
        mid = left + (right-left) / 2
        if nums[mid][0] == index:
            return mid
        elif nums[mid][0] < index:
            left = mid + 1
        else:
            right = mid - 1
    return -1


if __name__ == '__main__':
    A = [0 for _ in range(1000)]
    A[521] = 3
    A[234] = 2
    B = [2 for _ in range(1000)]

    print sparse_vector_product(A, B)

"""
If both are super sparse, go with hash table and product can be computed in O(m+n) time, where m, n are the number of non-zero 
entries in the two arrays respectively. If one of the array is dense, say B, then it is more efficient to use binary search 
so that product can be computed in O(mlogn) time.
"""
