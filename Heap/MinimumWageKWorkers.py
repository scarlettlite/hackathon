import heapq
class Solution():
    def mincostToHireWorkers(self, quality, wage, K):
        from fractions import Fraction
        workers = sorted((Fraction(w, q), q, w)
                         for q, w in zip(quality, wage))

        ans = float('inf')
        pool = []
        sumq = 0
        for ratio, q, w in workers:
            heapq.heappush(pool, -q)
            sumq += q

            if len(pool) > K:
                sumq += heapq.heappop(pool)
            """
            There is no guarantee that current employee is actually included in the heap
            but as we go further in this sorted array ratios increase ans so does the quality
            this means that we have already see a smaller value and the correctness of
            the larger value doesnt matter
            """
            if len(pool) == K:
                ans = min(ans, ratio * sumq)
            """
            if a person with a high ratio is getting paid his minimum so will 
            the persons smaller the ratio then them
            """

        return float(ans)

print(Solution().mincostToHireWorkers([10,5,4,3,2,6], [9,1,1,1,1,1], 3))
        