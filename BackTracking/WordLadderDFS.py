from collections import defaultdict, deque
class Solution:
    def __init__(self):
        self.ans = []
    def creategraph(self, words):
        graph = defaultdict(list)
        for i,x in enumerate(words):
            for y in words[i+1:]:
                if x != y:
                    if [a != b for a,b in zip(x,y)].count(True) == 1:
                        graph[x].append(y)
                        graph[y].append(x)
        return graph

    def helper(self, graph, visited, word, path, des):
        visited.add(word)
        path.append(word)
        if len(self.ans) > 0 and len(path) > len(self.ans[-1]):
            visited.remove(word)
            path.pop()
            return 
        if word == des:
            if len(self.ans) > 0 and len(self.ans[-1]) > len(path):
                self.ans.clear()
            self.ans.append(path[:])
            visited.remove(word)
            path.pop()
        else:
            for v in graph[word]:
                if v not in visited:
                    self.helper(graph, visited, v, path, des)
            visited.remove(word)
            path.pop()
        
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        wordList = list(set(wordList) | set([beginWord]))
        graph = self.creategraph(wordList)
        self.helper(graph, set(), beginWord, [], endWord)
        return self.ans


print(Solution().findLadders('hit', 'cog', ["hot","dot","dog","lot","log","cog"]))