"""
Return any binary tree that matches the given preorder and postorder traversals.

Values in the traversals pre and post are distinct positive integers.

 

Example 1:

Input: pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]
 

Note:

1 <= pre.length == post.length <= 30
pre[] and post[] are both permutations of 1, 2, ..., pre.length.
It is guaranteed an answer exists. If there exists multiple answers, you can return any of them.
"""

"""
The idea is to use two pointers, preIndex and postIndex, to traverse the pre and post array. The preIndex indicates the root 
node value. The key is that, when root.val == post[postIndex], we have completely constructed the subtree rooted at the current 
root node. We need to return that node, and increment the postIndex by 1.

Recursively solution: Time: O(n), Space: O(height).
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    preIndex, postIndex = 0, 0
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        root = TreeNode(pre[self.preIndex])
        self.preIndex += 1
        if root.val != post[self.postIndex]:
            root.left = self.constructFromPrePost(pre, post)
        if root.val != post[self.postIndex]:
            root.right = self.constructFromPrePost(pre, post)
        self.postIndex += 1
        return root

# Iterative Solution. Time: O(n), Space: O(height).
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        stack = [TreeNode(pre[0])]
        postIndex = 0
        for v in pre[1:]:
            node = TreeNode(v)
            while stack[-1].val == post[postIndex]:
                stack.pop()
                postIndex += 1
            if not stack[-1].left:
                stack[-1].left = node
            else:
                stack[-1].right = node
            stack.append(node)
        return stack[0]
