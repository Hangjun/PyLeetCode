"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary search tree can be serialized to a string and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
"""

"""
The difference between this problem and https://leetcode.com/problems/serialize-and-deserialize-binary-tree/ is that now we need 
to use the BST structure to keep the encoding as compact as possible. We can omit the '#' for the empty child nodes. In the 
decoding phase, we use a stack to re-construct the tree in O(n) time.

Time: O(n), Space: O(n).
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def preorder(root):
            if not root: return
            res.append(str(root.val))
            preorder(root.left)
            preorder(root.right)
        
        res = []
        preorder(root)
        return ' '.join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        preorder = map(int, data.split())
        stack = []
        root = None
        for val in preorder:
            curNode = TreeNode(val)
            if not root:
                root = curNode
            else:
                if val < stack[-1].val:
                    stack[-1].left = curNode
                else:
                    while stack and stack[-1].val < val:
                        parentNode = stack.pop()
                    parentNode.right = curNode
            stack.append(curNode)
        return root
                    

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
