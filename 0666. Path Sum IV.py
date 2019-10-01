"""
If the depth of a tree is smaller than 5, then this tree can be represented by a list of three-digits integers.

For each integer in this list:

The hundreds digit represents the depth D of this node, 1 <= D <= 4.
The tens digit represents the position P of this node in the level it belongs to, 1 <= P <= 8. The position is the same as that in a full binary tree.
The units digit represents the value V of this node, 0 <= V <= 9.
 

Given a list of ascending three-digits integers representing a binary tree with the depth smaller than 5, you need to return the sum of all paths from the root towards the leaves.

Example 1:

Input: [113, 215, 221]
Output: 12
Explanation: 
The tree that the list represents is:
    3
   / \
  5   1

The path sum is (3 + 5) + (3 + 1) = 12.
 

Example 2:

Input: [113, 221]
Output: 4
Explanation: 
The tree that the list represents is: 
    3
     \
      1

The path sum is (3 + 1) = 4.
"""

"""
If we know what the tree looks like, we can use DFS to traverse the tree and get the total sum:
  def: dfs(self, root, curSum):
    if not root:
      return 0
    curSum += root.val
    if not root.left and not root.right:
      return curSum
    return self.dfs(root.left, curSum) + self.dfs(root.right, curSum)
    
If we can construct the tree from the input then problem solved. It turns out that we can use a hash table to construct the tree: 
given a node that's in the format of xyz, x indicates the level, y indicates the position, and z is the value. We can use xy as 
the key and z as the value. The left child is then (2x)(2y-1)? and right child is (2x)(2y)?. This gives us the tree.

DFS + Hash Table. Time: O(n), Space: O(n). 2 Pass Solution.
"""
from collections import defaultdict

class Solution(object):
    def pathSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        tree = defaultdict(int)
        for n in nums:
            tree[n / 10] = n % 10
        return self.dfs(tree, nums[0]/10, 0)
    
    def dfs(self, tree, curNode, curSum):
        if curNode not in tree:
            return 0
        level, pos, val = curNode / 10, curNode % 10, tree[curNode]
        left = (level + 1) *10 + 2 * pos - 1
        right = (level + 1) * 10 + 2 * pos
        
        curSum += val
        if left not in tree and right not in tree:
            return curSum
        return self.dfs(tree, left, curSum) + self.dfs(tree, right, curSum)
