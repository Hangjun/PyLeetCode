"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""

# Heap Sort. n = len(lists), k = average length of a list. Time: O(nklogn), Space: O(n).
from heapq import heapify, heappush, heappop
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        dummyNode = ListNode(-1)
        head = dummyNode
        heap = [(ln.val, ln) for ln in lists if ln]
        heapify(heap)
        while heap:
            val, curList = heappop(heap)
            head.next = ListNode(val)
            head = head.next
            if curList.next:
                heappush(heap, (curList.next.val, curList.next))
        
        return dummyNode.next
