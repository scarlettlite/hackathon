import math
class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {string}
    def getPermutation(self, n, k):
        numbers = list(range(1, n+1))
        permutation = ''
        """
        example: n = 4, k = 9, here k is 1-indexed,
        so subtract 1 from k to make it zero indexed
        if k is 0-5: then permutation starts with '1'
        if k is 6-11: then permutation starts with '2'
        if k is 12-17: then permutation starts with '3'
        if k is 18-23: then permutation starts with '4'
        """
        k -= 1
        fact = math.factorial(n)
        while n > 0:
            fact //= n
            n -= 1
            # get the index of current digit
            index, k = divmod(k, fact)
            permutation += str(numbers[index-1])
            # remove handled number
            numbers.remove(numbers[index])

        return permutation

print(Solution().getPermutation(4, 9))