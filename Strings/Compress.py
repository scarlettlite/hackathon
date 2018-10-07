class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        read, write = 0, 0
        n = len(chars)
        while read < n:
            j = read + 1
            print(j,n)
            while j < n and chars[j-1] == chars[j]:
                j += 1
            if j <= n and j - read > 1:
                count = j - read
                count = list(str(count))
                chars[read:j] = count
                write += 1 + len(count)
            read = j
        return write

print(Solution().compress(["a","a","b","b","c","c","c"]))