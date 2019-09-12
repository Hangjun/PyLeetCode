"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""

# Two Pointers. Time: O(m+n), Additional Space: O(1)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = head = ListNode(-1)
        node1, node2 = l1, l2
        while (node1 or node2):
            if not node1:
                head.next = node2
                break
            elif not node2:
                head.next = node1
                break
            elif node1.val > node2.val:
                head.next = ListNode(node2.val)
                head = head.next
                node2 = node2.next
            else:
                head.next = ListNode(node1.val)
                head = head.next
                node1 = node1.next
        return dummy.next
