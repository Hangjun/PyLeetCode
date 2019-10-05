"""
Given the root of a tree, you are asked to find the most frequent subtree sum. The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself). So what is the most frequent subtree sum value? If there is a tie, return all the values with the highest frequency in any order.

Examples 1
Input:

  5
 /  \
2   -3
return [2, -3, 4], since all the values happen only once, return all of them in any order.
Examples 2
Input:

  5
 /  \
2   -5
return [2], since 2 happens twice, however -5 only occur once.
Note: You may assume the sum of values in any subtree is in the range of 32-bit signed integer.
"""

# DFS. Time: O(n), Space: O(n).
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        # subtree sum histogram
        sum_map = collections.Counter()
        self.dfs(root, sum_map)
        max_count = max(sum_map.values())
        return [k for k in sum_map if sum_map[k] == max_count]
    
    def dfs(self, cur_node, sum_map):
        if not cur_node:
            return 0
        left_sum = self.dfs(cur_node.left, sum_map)
        right_sum = self.dfs(cur_node.right, sum_map)
        cur_sum = left_sum + right_sum + cur_node.val
        sum_map[cur_sum] += 1
        return cur_sum
