"""
You have n binary tree nodes numbered from 0 to n - 1 where node i has two children leftChild[i] and rightChild[i], return true if and only if all the given nodes form exactly one valid binary tree.

If node i has no left child then leftChild[i] will equal -1, similarly for the right child.

Note that the nodes have no values and that we only use the node numbers in this problem.

 

Example 1:



Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
Output: true
Example 2:



Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
Output: false
Example 3:



Input: n = 2, leftChild = [1,0], rightChild = [-1,-1]
Output: false
Example 4:



Input: n = 6, leftChild = [1,-1,-1,4,-1,-1], rightChild = [2,-1,-1,5,-1,-1]
Output: false
 

Constraints:

1 <= n <= 10^4
leftChild.length == rightChild.length == n
-1 <= leftChild[i], rightChild[i] <= n - 1
"""

"""
The data format is more complicated than the problem itself. It is a valid binary tree if and only if 1) there is no directed 
cycles and 2) there is only root, i.e. the tree must be connected. We traverse the left and right child array and record the 
parents of each node. Effectively we are establishing a directed edge from parent -> left/rightChild. We use a visited set to 
remember the left/right child that have been visited so far. If we are visiting a visited node, then the indegree of that node 
exceeds one, meaning that there are two parents having this node as a child which violates the tree structure. 

After we have established the parent table, all we need to do is to find the root. The root is defined as the node whose parent 
does not exist. We need to have exactly one such node.

Time: O(n), Space: O(n).
"""
class Solution(object):
    def validateBinaryTreeNodes(self, n, leftChild, rightChild):
        """
        :type n: int
        :type leftChild: List[int]
        :type rightChild: List[int]
        :rtype: bool
        """
        if n <= 1:
            return True
        
        visited = set()
        parent = [-1 for i in range(n)]
        for i in range(n):
            if leftChild[i] in visited or rightChild[i] in visited:
                return False
            if leftChild[i] != -1:
                visited.add(leftChild[i])
                parent[leftChild[i]] = i
            if rightChild[i] != -1:
                visited.add(rightChild[i])
                parent[rightChild[i]] = i
        
        rootCount = 0
        for i in range(n):
            if parent[i] == -1:
                if leftChild[i] == -1 and rightChild[i] == -1:
                    continue
                rootCount += 1
        return rootCount == 1

