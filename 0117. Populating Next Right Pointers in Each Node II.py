"""
Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

 

Follow up:

You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.
 

Example 1:



Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
 

Constraints:

The number of nodes in the given tree is less than 6000.
-100 <= node.val <= 100
"""

# Same as Problem 116. Time: O(n), Space: O(1).
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        lastHead = root
        curHead = None
        curNode = Node()
        while lastHead:
            lastCur = lastHead
            while lastCur:
                if lastCur.left:
                    if not curHead:
                        curHead = lastCur.left
                        curNode = curHead
                    else:
                        curNode.next = lastCur.left
                        curNode = curNode.next
                if lastCur.right:
                    if not curHead:
                        curHead = lastCur.right
                        curNode = curHead
                    else:
                        curNode.next = lastCur.right
                        curNode = curNode.next
                lastCur = lastCur.next
            lastHead = curHead
            curHead = None
        return root
