"""
Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: []

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""

"""
Since we need to return all possible shortest paths, we cannot use a visited set to skip a word that's already been visited, since 
that might also lead to a shortest path. However, we also do not want to run into a cycle by visiting the same word over and over 
again. The solution is to minic Dijkstra's algorthm and use a distance[] set to record the shortest distance from beginWord. 
We add the next word to the BFS queue if and only if we can improve its distance by going from current word to it. However, if 
distance[nextWord] == distance[curWord] + 1, we also need to record it since we have just discovered an alternative route.

BFS + DFS. Time: O(nk), Space: O(nk), n = number of words, k = length of word.
"""
from collections import deque, defaultdict
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        self.res = []
        if not beginWord or not endWord or not wordList or endWord not in wordList:
            return self.res
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                template = word[:i] + '*' + word[i+1:]
                all_combo_dict[template].append(word)
        
        queue = deque([beginWord])
        
        # minimum distance from beginWord - we use this to detect whether a word was visited before
        distance = defaultdict(int)
        for word in wordList:
            distance[word] = sys.maxint
        distance[beginWord] = 0
        parent = defaultdict(set)
        found = False
        # BFS to establish all the shortest path links from beginWord to endWord
        while queue:
            curWord = queue.popleft()
            if curWord == endWord:
                found = True
            for i in range(len(curWord)):
                template = curWord[:i] + '*' + curWord[i+1:]
                for word in all_combo_dict[template]:
                    if distance[word] == sys.maxint:
                        parent[word].add(curWord)
                        queue.append(word)
                        distance[word] = distance[curWord] + 1
                    elif distance[word] == distance[curWord] + 1: # found an alternative shortest path
                        parent[word].add(curWord)
        if found:
            self.retrievePaths(beginWord, endWord, [endWord], parent)
        return self.res
    
    # Backtrack to find all the paths
    def retrievePaths(self, beginWord, endWord, path, parent):
        print('curPath = {}'.format(path))
        if endWord == beginWord:
            self.res.append(path[::-1])
            return
        # DFS on the parent words of endWord
        for parentWord in parent[endWord]:
            self.retrievePaths(beginWord, parentWord, path+[parentWord], parent)
