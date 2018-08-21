import random, string
class Codec:
    def __init__(self):
        """
        Use strings existing constanst to generate an alphabet set
        """
        self.dd = {}
        self.alphabets = string.digits + string.ascii_letters

    def getrandom(self):
        key = []
        for _ in range(6):
            """
            use random.randint to generate a random
            number integer in a range [a,b]
            """
            key.append(self.alphabets[random.randint(0,61)%62])
        return ''.join(key)

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        key = self.getrandom()
        while key in self.dd:
            key = self.getrandom()
        self.dd[key] = longUrl
        return 'http://tinyurl.com/'+key

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        key = shortUrl[shortUrl.rindex('/') + 1:]
        return self.dd[key]
codec = Codec()
x = codec.encode('https://leetcode.com/problems/design-tinyurl')
print(x)
print(codec.decode(x))

"""
1.The number of URLs that can be encoded is quite large in this case, nearly 
    of the order (10+26*2)^6
2.The length of the encoded URLs is fixed to 6 units, which is a significant 
    reduction for very large URLs.
3.The performance of this scheme is quite good, due to a very less probability 
    of repeated same codes generated.
4.We can increase the number of encodings possible as well, by increasing the 
    length of the encoded strings. Thus, there exists a tradeoff between the 
    length of the code and the number of encodings possible.
5.Predicting the encoding isn't possible in this scheme since random numbers are used.
"""