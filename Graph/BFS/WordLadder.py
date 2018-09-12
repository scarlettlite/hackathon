from collections import defaultdict, deque
class defaultInfDict(dict):
    def __missing__(self, key):
        self[key] = float('inf')
        return float('inf')

class Solution:
    def isdisone(self, word1, word2):
        return sum(1 for a,b in zip(word1, word2) if a!=b) == 1

    def creategraph(self, wordList, beginWord, endWord):
        wordList = list(set(wordList) | {beginWord})
        graph = defaultdict(list)
        n = len(wordList)
        for i in range(n):
            for j in range(i+1, n):
                if self.isdisone(wordList[i], wordList[j]):
                    graph[wordList[i]].append(wordList[j])
                    graph[wordList[j]].append(wordList[i])
        return wordList, graph

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordList, graph = self.creategraph(wordList, beginWord, endWord)
        queue = deque([(1, beginWord)])
        disdict = defaultInfDict({beginWord:1})
        while queue:
            dis, word = queue.popleft()
            if word == endWord:
                return dis
            if disdict[word] < dis:
                continue
            for neighbor in graph[word]:
                if dis + 1 < disdict[neighbor]:
                    queue.append((dis+1, neighbor))
                    disdict[neighbor] = dis + 1
        return 0

print(Solution().ladderLength("qa",
"sq",
["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]))