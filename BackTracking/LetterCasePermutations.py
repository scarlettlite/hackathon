class Solution:

    def helper(self, s, index, visited):
        ans = []
        if s not in visited:
            ans.append(s)
            visited.add(s)
        for i in range(index, len(s)):
            if s[i].isalpha():
                news = s[:i] + s[i].lower() + s[i+1:]
                ans.extend(self.helper(news, i+1, visited))
                news = s[:i] + s[i].upper() + s[i+1:]
                ans.extend(self.helper(news, i+1, visited))
            else:
                ans.extend(self.helper(s, i+1, visited))
        return ans


    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        visited = set()
        return self.helper(S, 0, visited)
            

print(Solution().letterCasePermutation(""))