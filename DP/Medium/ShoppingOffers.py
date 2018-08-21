class Solution:
    def find_lowest_price(self, price, special, needs):
        x = tuple(needs)
        if x in self.dp:
            return self.dp[x]
        else:
            cost = 0
            for n, p in zip(needs, price):
                cost += n*p
            for offer in special:
                for i,n in enumerate(needs):
                    if offer[i] > needs[i]:
                        break
                else:
                    newneeds = [needs[i] - offer[i] for i in range(len(needs))]
                    cost = min(cost, offer[-1] + self.find_lowest_price(price, special, newneeds))
            return cost
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        self.dp = {}
        return self.find_lowest_price(price, special, needs)

print(Solution().shoppingOffers([2,3,4], [[1,1,0,4],[2,2,1,9]], [1,2,1]))