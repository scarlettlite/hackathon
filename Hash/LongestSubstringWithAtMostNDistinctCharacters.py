class Solution:
    class Solution:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :rtype: int
        """
        if not s or k == 0 : return 0
        ss = {}
        i, n , ans = 0, len(s), 0
        beg, end = 0, 0
        while i<n and (len(ss.keys()) < k or s[i] in ss):
            ss[s[i]] = i
            i += 1
        end = i-1
        ans = end - beg + 1
        if i < n:
            while i < n:
                if s[i] not in ss:
                    l, k = 0, None
                    for key in ss.keys():
                        t = end - ss[key]
                        if l <= t:
                            l = t
                            beg = ss[key] + 1
                            k = key
                    del ss[k]
                ss[s[i]] = i
                end = i
                i += 1
                ans = max(ans, end - beg + 1)
        return ans

print(Solution().lengthOfLongestSubstringTwoDistinct(""))