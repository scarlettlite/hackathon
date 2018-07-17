import heapq
class Solution:
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        uglies = [1]
        heap = [(prime,i) for i,prime in enumerate(primes)]
        indx = [0 for _ in primes]
        while len(uglies) < n:
            value, i = heapq.heappop(heap)
            indx[i] +=1
            if value > uglies[-1]:
                uglies.append(value)
            """
            In Brute force when we pop a number from the heap
            we multiply by all primes one by one and push the results onto the 
            heap. in this optimal approach we track the ugly number that will
            be used to obtain the next ugly number when mutiplied with a
            particular prime
            """
            heapq.heappush(heap, (primes[i]*uglies[indx[i]],i))
                
        return uglies[-1]

print(Solution().nthSuperUglyNumber(12, [2,7,13,19]))