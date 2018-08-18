class Solution:
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        
        s = ' '.join(sentence) + ' '
        dp = [0 for _ in range(len(s))]
        for i in range(1, len(s), 1):
            if s[i] == ' ':
                dp[i] = 1
            else:
                dp[i] = dp[i-1] - 1
                
        start, l = 0, len(s)
        for _ in range(rows):
            start += cols
            start += dp[start % l]
        return start // l
            
print(Solution().wordsTyping(["a","bcd"],
20000,
20000))