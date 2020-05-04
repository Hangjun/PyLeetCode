"""
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""

# Solution #1: BFS from beingWord. Time: O(nk), Space: O(nk), where n = number of words, k = len(word)
from collections import deque, defaultdict
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if not endWord or not beginWord or not wordList or endWord not in wordList:
            return 0
        k = len(beginWord)
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(k):
                template = word[:i] + '*' + word[i+1:]
                all_combo_dict[template].append(word)
        visited = set()
        queue = deque([(beginWord, 1)])
        visited.add(beginWord)
        while queue:
            curWord, dist = queue.popleft()
            if curWord == endWord:
                return dist
            # BFS on its neighbor words
            for i in range(k):
                template = curWord[:i] + '*' + curWord[i+1:]
                print('template = {}'.format(template))
                for word in all_combo_dict[template]:
                    if word not in visited:
                        visited.add(word)
                        print('add {}'.format(word))
                        queue.append((word, dist+1))
                # erase the values for this template
                all_combo_dict[template] = []
        return 0
    
# We can minic a Dijkstra's algorithm flavor and use a distance array to record the minimum distance from beginWord and use that 
# to detect words that have been visited before:
from collections import deque, defaultdict
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if not endWord or not beginWord or not wordList or endWord not in wordList:
            return 0
        k = len(beginWord)
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(k):
                template = word[:i] + '*' + word[i+1:]
                all_combo_dict[template].append(word)
        distance = defaultdict(int)
        for word in wordList:
            distance[word] = sys.maxint
        distance[beginWord] = 1
        queue = deque([(beginWord)])
        while queue:
            curWord= queue.popleft()
            if curWord == endWord:
                return distance[curWord]
            # BFS on its neighbor words
            for i in range(k):
                template = curWord[:i] + '*' + curWord[i+1:]
                for word in all_combo_dict[template]:
                    if distance[word] == sys.maxint:
                        distance[word] = distance[curWord]+1
                        queue.append((word))
                # erase the values for this template for faster branch cuts
                all_combo_dict[template] = []
        return 0

"""
The graph formed from the nodes in the dictionary might be too big. The search space considered by the breadth first search 
algorithm depends upon the branching factor of the nodes at each level. If the branching factor remains the same for all the 
nodes, the search space increases exponentially along with the number of levels. Consider a simple example of a binary tree. 
With each passing level in a complete binary tree, the number of nodes increase in powers of 2.

We can considerably cut down the search space of the standard breadth first search algorithm if we launch two simultaneous BFS. 
One from the beginWord and one from the endWord. We progress one node at a time from both sides and at any point in time if we 
find a common node in both the searches, we stop the search. This is known as bidirectional BFS and it considerably cuts down 
on the search space and hence reduces the time and space complexity.

Algorithm

1. The algorithm is very similar to the standard BFS based approach we saw earlier.

2. The only difference is we now do BFS starting two nodes instead of one. This also changes the termination condition of our 
search.

3. We now have two visited dictionaries to keep track of nodes visited from the search starting at the respective ends.

4. If we ever find a node/word which is in the visited dictionary of the parallel search we terminate our search, since we 
have found the meet point of this bidirectional search. It's more like meeting in the middle instead of going all the way 
through. Termination condition for bidirectional search is finding a word which is already been seen by the parallel search.

5. The shortest transformation sequence is the sum of levels of the meet point node from both the ends. Thus, for every visited 
node we save its level as value in the visited dictionary.
"""
# Solution #2: Bidirectional BDS. Time: O(nk), Space: O(nk).
from collections import deque, defaultdict
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if not endWord or not beginWord or not wordList or endWord not in wordList:
            return 0
        k = len(beginWord)
        self.all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(k):
                template = word[:i] + '*' + word[i+1:]
                self.all_combo_dict[template].append(word)
        visited_begin = {beginWord:1}
        visited_end = {endWord:1}
        queue_begin = deque([(beginWord, 1)])
        queue_end = deque([(endWord, 1)])
        res = None
        while queue_begin and queue_end:
            res = self.bfs(queue_begin, visited_begin, visited_end)
            if res:
                return res
            res = self.bfs(queue_end, visited_end, visited_begin)
            if res:
                return res
        return 0

    def bfs(self, queue, visited, otherVisited):
        curWord, dist = queue.popleft()
        if curWord in otherVisited:
            return dist + otherVisited[curWord] - 1 # double counted the distances on both sides
        # BFS on its neighbor words
        for i in range(len(curWord)):
            template = curWord[:i] + '*' + curWord[i+1:]
            for word in self.all_combo_dict[template]:
                if word not in visited:
                    visited[word] = dist + 1
                    queue.append((word, visited[word]))
            self.all_combo_dict[template] = []
        return None

