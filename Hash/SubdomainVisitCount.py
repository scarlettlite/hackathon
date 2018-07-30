from collections import defaultdict
class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        dd = defaultdict(int)
        for x in cpdomains:
            hits, domain = x.split(' ')
            hits = int(hits)
            dd[domain] += hits
            i = domain.rindex('.')
            dd[domain[i+1:]] += hits
            j = domain.index('.')
            if i != j:
                dd[domain[j+1:]] += hits
        ans = []
        for key, value in dd.items():
            ans.append(str(value) +' '+ key)
        return ans

print(Solution().subdomainVisits(["9001 discuss.leetcode.com"]))