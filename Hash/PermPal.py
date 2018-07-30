"""
https://leetcode.com/problems/palindrome-permutation/description/
"""
from collections import Counter
class Solution:
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return [False if value%2 == 1 else True for key, value in Counter(s).items].count(True) > 1
        