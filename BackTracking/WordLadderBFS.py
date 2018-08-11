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

    def bfs(self, beginWord, graph, endWord):
        queue = deque([(beginWord, [], set())])
        flag = True
        while queue and flag:
            qsize = len(queue)
            for _ in range(qsize):
                u, path, visited = queue.popleft()
                if u in visited and u == endWord: continue
                path.append(u)
                visited.add(u)
                if u == endWord:
                    flag = False
                    self.ans.append(path)
                visited.add(u)
                for v in graph[u]:
                    if v not in visited:
                        queue.append((v, path[:], visited.copy()))
        return

        
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        wordList = list(set(wordList) | set([beginWord]))
        graph = self.creategraph(wordList)
        self.bfs(beginWord, graph, endWord)
        return self.ans

print(Solution().findLadders("red",
"tax",
["ted","tex","red","tax","tad","den","rex","pee"]))