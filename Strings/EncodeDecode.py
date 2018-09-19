class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        ans = ' '.join(strs)
        x,y = ans[::2],ans[1::2]
        return x+y
        

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        n2 = (n+ 1)//2
        x,y = s[:n2],s[n2:]
        ans = [None for _ in range(n)]
        ans[::2], ans[1::2] = x,y
        a = ''.join(ans)
        b = a.split(' ')
        return b

cod = Codec()
x = cod.encode([])
print(x)
y = cod.decode(x)
print(y)