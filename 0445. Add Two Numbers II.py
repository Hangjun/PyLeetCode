"""
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
"""

# Time: O(n), Space: O(n).
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        stack1 = []
        stack2 = []
        curNode = l1
        while curNode:
            stack1.append(curNode.val)
            curNode = curNode.next
        curNode = l2
        while curNode:
            stack2.append(curNode.val)
            curNode = curNode.next
        
        carry = 0
        res = []
        while stack1 or stack2 or carry:
            if stack1:
                carry += stack1.pop()
            if stack2:
                carry += stack2.pop()
            res.append(carry % 10)
            carry /= 10
        dummyNode = ListNode(-1)
        curNode = dummyNode
        for val in res[::-1]:
            curNode.next = ListNode(val)
            curNode = curNode.next
        return dummyNode.next
