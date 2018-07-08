class Solution:
    def replaceWords(self, dicti, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        if not dicti or not sentence : return sentence
        worddict = set(dicti)
        words = sentence.split()
        for i,word in enumerate(words):
            root = word
            for j in range(0, len(word)):
                prefix = word[:j]
                if prefix in worddict:
                    root = min(root, word)
            #print(root)
            words[i] = root
        return ' '.join(words)

