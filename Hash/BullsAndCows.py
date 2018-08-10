class Solution:
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        #lengths are equal 
        bulls = cows = 0            #counters 
        
        from collections import defaultdict 
        eSecret = defaultdict(int)
        eGuess = defaultdict(int)

        for sChar, gChar in zip(secret,guess): 
            if sChar == gChar: 
                bulls += 1 
            else: 
                eSecret[sChar] += 1
                eGuess[gChar] += 1

        for sChar in eSecret.keys(): 
            cows += min(eSecret[sChar],eGuess[sChar])
        
        return str(bulls) + "A" + str(cows) + "B" 

print(Solution().getHint("1123", "0111"))