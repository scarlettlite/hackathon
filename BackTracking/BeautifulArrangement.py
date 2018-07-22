""""
Has Performance Issues
""""

class Solution:
    def __init__(self):
        self.count = 0
        
    def helper(self, array, index):
        if index == len(array):
            self.count +=1
        else:
            for i in range(index, len(array)):
                array[index], array[i] = array[i], array[index]
                if array[index]%(index+1) == 0 or (index+1)%array[index] == 0:
                    self.helper(array, index+1) 
                array[index], array[i] = array[i], array[index]

    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        if not N : return 0
        self.helper([i+1 for i in range(N)],0)
        return self.count

print(Solution().countArrangement(15))