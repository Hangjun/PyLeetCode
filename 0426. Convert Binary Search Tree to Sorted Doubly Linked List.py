"""
Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.

You can think of the left and right pointers as synonymous to the predecessor and successor pointers in a doubly-linked list. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.

We want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. You should return the pointer to the smallest element of the linked list.

 

Example 1:



Input: root = [4,2,5,1,3]


Output: [1,2,3,4,5]

Explanation: The figure below shows the transformed BST. The solid line indicates the successor relationship, while the dashed line means the predecessor relationship.

Example 2:

Input: root = [2,1,3]
Output: [1,2,3]
Example 3:

Input: root = []
Output: []
Explanation: Input is an empty tree. Output is also an empty Linked List.
Example 4:

Input: root = [1]
Output: [1]
 

Constraints:

-1000 <= Node.val <= 1000
Node.left.val < Node.val < Node.right.val
All values of Node.val are unique.
0 <= Number of Nodes <= 2000
"""

"""
The problem description is overly complicated. It essentially boils down to traverse the BST inorder and establish the links 
along the way, i.e. in-place.
"""

# Iterative Solution. Time: O(n), Space: O(logn).
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        self.prev = None
        self.head = None
        self.inorder(root)
        self.head.left = self.prev
        self.prev.right = self.head
        return self.head
    
    def inorder(self, root):
        stack = []
        cur = root
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                if not self.prev:
                    self.head = cur # find the head of the list
                else:
                    self.prev.right = cur
                    cur.left = self.prev
                self.prev = cur
                cur = cur.right

# Recursive Inorder Traversal: Time: O(n), Space: O(logn).
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        self.prev = None
        self.head = None
        self.inorder(root)
        self.head.left = self.prev
        self.prev.right = self.head
        return self.head
    
    def inorder(self, curNode):
        if not curNode:
            return
        self.inorder(curNode.left)
        if not self.prev:
            self.head = curNode # find the head of the linked list
        else:
            self.prev.right = curNode
            curNode.left = self.prev
        self.prev = curNode
        self.inorder(curNode.right)
