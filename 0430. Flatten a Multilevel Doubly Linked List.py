"""
You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer, which may or may not point to a separate doubly linked list. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure, as shown in the example below.

Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first level of the list.

 

Example 1:

Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
Output: [1,2,3,7,8,11,12,9,10,4,5,6]
Explanation:

The multilevel linked list in the input is as follows:



After flattening the multilevel linked list it becomes:


Example 2:

Input: head = [1,2,null,3]
Output: [1,3,2]
Explanation:

The input multilevel linked list is as follows:

  1---2---NULL
  |
  3---NULL
Example 3:

Input: head = []
Output: []
 

How multilevel linked list is represented in test case:

We use the multilevel linked list from Example 1 above:

 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL
The serialization of each level is as follows:

[1,2,3,4,5,6,null]
[7,8,9,10,null]
[11,12,null]
To serialize all levels together we will add nulls in each level to signify no node connects to the upper node of the previous level. The serialization becomes:

[1,2,3,4,5,6,null]
[null,null,7,8,9,10,null]
[null,11,12,null]
Merging the serialization of each level and removing trailing nulls we obtain:

[1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
 

Constraints:

Number of Nodes will not exceed 1000.
1 <= Node.val <= 10^5
"""

"""
This problem is much simplier than it appears to be. The goal is to traverse the doubly linked list and "insert" the child branch 
into the original list. The key is to connect the last node of the child branch to the previous next node. To do we can can use a 
stack. We use two pointers, prev and cur, to traverse the linked list and push the next node onto the stack. If the next node 
exists, we push it onto the stack first; if there is a child node, we push that onto the stack second. The prev and cur will 
always follow the order of the stack pop, therefore it will first traverse the child branch completely while still remember where 
it left off prior to branching off - since we push the next node onto the stack first.

Time: O(n), Space: O(n).
"""
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        stack = [head]
        prevNode = Node(-1)
        while stack:
            curNode = stack.pop()
            curNode.prev = prevNode
            prevNode.next = curNode
            prevNode = curNode
            if curNode.next:
                stack.append(curNode.next)
            if curNode.child:
                stack.append(curNode.child)
                curNode.child = None
        head.prev = None
        return head
