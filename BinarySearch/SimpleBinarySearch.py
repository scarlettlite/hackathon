from random import randint
class Solution:
    def binarysearch(self, nums, key):
        print('tofind = ', key)
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high)//2
            if nums[mid] < key:
                low = mid + 1
            else:
                high = mid
        if nums[low] == key:
            print("Found ", nums[low])
        else:
            print("Search Unsuccessful")  
    
    def sameOrNextGreater(self, nums, key):
        print('tofind = ', key)
        low, high = 0, len(nums) - 1
        while low < high:
            """
            In case low + 1 == high, which is the base case, mid is always = low
            and when we do high = mid , high = mid = low, the loop ends
            """
            mid = (low + high)//2
            if nums[mid] < key:
                low = mid + 1
            else:
                high = mid
        # since no greater number 
        if nums[low] < key:
            print("Search Unsuccessful")  
        print("Found ", nums[low])
        """
        When we come out of the loop low is always equal to high, so we can pick either low or
        high. For Consistency we pick low. 
        """

    def sameOrNextSmaller(self, nums, key):
        print('toFind', key)
        low, high = 0 , len(nums) - 1
        while low < high:
            """
            In case low == high + 1, we need to move low towards high. adding 1 in the statement
            ensures that in this case mid = high, so that when we do low = mid, we have
            low = mid = high and the loop breaks
            """
            mid = (low + high) // 2 + 1
            if nums[mid] > key:
                high = mid - 1
            else:
                low = mid
        if nums[low] > key:
            print("Search Unsuccessful")  
        print("Found ", nums[low])

    def nextGreater(self, nums, key):
        print('toFind', key)
        key += 1
        self.sameOrNextGreater(nums, key)
    
    def nextSmaller(self, nums, key):
        print('toFind', key)
        key -= 1
        self.sameOrNextSmaller(nums, key)

    def positioninsortednums(self, nums, key):
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high)// 2
            if nums[mid] < key:
                low = mid + 1
            else:
                high = mid
        ans = low
        if nums[low] < key:
            ans = low + 1
        elif nums[low] > key:
            ans = 0
        print(ans)






nums = [ 3, 7, 8 ,9, 14, 19, 23, 34, 39, 41, 48, 52]
nums.sort()
# Solution().sameOrNextGreater(nums, 8)
# Solution().sameOrNextGreater(nums, 10)
# Solution().sameOrNextGreater(nums, 20)
# Solution().sameOrNextGreater(nums, 4)
# Solution().sameOrNextGreater(nums, 70)
# Solution().sameOrNextGreater(nums, 1)

# Solution().sameOrNextSmaller(nums, 10)
# Solution().sameOrNextSmaller(nums, 20)
# Solution().sameOrNextSmaller(nums, 4)
# Solution().sameOrNextSmaller(nums, 70)
# Solution().sameOrNextSmaller(nums, 1)

# Solution().nextGreater(nums, 10)
# Solution().nextGreater(nums, 22)
# Solution().nextGreater(nums, 6)
# Solution().nextGreater(nums, 70)
# Solution().nextGreater(nums, 1)

Solution().nextSmaller(nums, 10)
Solution().nextSmaller(nums, 24)
Solution().nextSmaller(nums, 3)
Solution().nextSmaller(nums, 70)
Solution().nextSmaller(nums, 1)
