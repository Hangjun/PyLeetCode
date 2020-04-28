"""
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
"""

# Solution #1. Recursively find the middle element. Time: O(nlogn), Space: O(logn).
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        mid = self.findMiddle(head)
        root = TreeNode(mid.val)
        
        # only one element in the linked list
        if mid == head:
            return root
        
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)
        return root
    
    def findMiddle(self, head):
        if not head:
            return None
        prev = None
        slow, fast = head, head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        # cut off the left part of the list
        if prev:
            prev.next = None
        
        return slow
        
# Solution #2. Simulate inorder traversal. Time: O(n), Space: O(logn).
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        size = 0
        cur = head
        while cur:
            cur = cur.next
            size += 1
        self.head = head
        
        def helper(left, right):
            print left, right
            if left > right:
                return None
            mid = left + (right - left) / 2
            leftChild = helper(left, mid-1)
            root = TreeNode(self.head.val)
            self.head = self.head.next
            rightChild = helper(mid+1, right)
            root.left = leftChild
            root.right = rightChild
            return root
        
        return helper(0, size-1)
