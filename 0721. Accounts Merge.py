"""
Given a list accounts, each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some email that is common to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

Example 1:
Input: 
accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
Output: [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
Explanation: 
The first and third John's are the same person as they have the common email "johnsmith@mail.com".
The second John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
Note:

The length of accounts will be in the range [1, 1000].
The length of accounts[i] will be in the range [1, 10].
The length of accounts[i][j] will be in the range [1, 30].
"""

"""
This is a graph problem in disguise. More specifically, this is finding the connected component in an undirected graph. There is 
an edge between two emails if they belong to the same person. We first create the adjacency list representation of this graph, 
and then use BFS to find the connected components. One trick in constructing the adjacency list is that, since this is an 
undirected graph, we do not need to look at every single pair of emails. We only need to look at all pairs with the first email 
in every account and that would be sufficient to construct the graph.

Time: O(mnlogn), Space: O(mn), here a = average length of an account, m = total number of accounts.
"""
from collections import defaultdict, deque

class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        email_to_name = {}
        adj_list = defaultdict(list)
        for account in accounts:
            name = account[0]
            email_list = account[1:]
            if not email_list:
                continue
            first_email = email_list[0]
            for email in email_list:
                adj_list[first_email].append(email)
                adj_list[email].append(first_email)
                email_to_name[email] = name
        
        # traverse the adj_list and find the connected components
        visited = set()
        res = []
        for email in adj_list:
            if email in visited:
                continue
            visited.add(email)
            component = []
            queue = deque([email])
            # BFS from this email and find all reachable emails
            # invariant: emails in the queue are all visited but their neighbors might not
            while queue:
                curEmail = queue.popleft()
                component.append(curEmail)
                for nn in adj_list[curEmail]:
                    if nn not in visited:
                        visited.add(nn)
                        queue.append(nn)
            
            # add the current compoent in sorted order into res
            res.append([email_to_name[email]] + sorted(component))
        
        return res
