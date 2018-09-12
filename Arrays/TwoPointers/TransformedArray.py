class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        n = len(nums)
        result = [None]*n
        if a == 0:
            if b < 0:
                nums = nums[::-1]
            for i,x in enumerate(nums):
                result[i] = b * x + c
            return result
        pivot = -b / (2*a)
        low, high = 0, n-1
        end  = n - 1
        distance = [None]*n
        while low <= high:
            d1, d2 = pivot - nums[low], nums[high] - pivot
            print(d1,nums[low])
            print(d2,nums[high])
            if d1 > d2:
                distance[end] = nums[low]
                low += 1
            else:
                distance[end] = nums[high]
                high -= 1
            end -= 1
        print(distance)
        if a < 0:
            distance = distance[::-1]
        print(distance)
        result = [None]*n
        for i,x in enumerate(distance):
            result[i] = a * x * x + b * x + c
            
        return result

print(Solution().sortTransformedArray([-4,-2,2,4],
-1,
3,
5))

