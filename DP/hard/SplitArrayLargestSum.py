class Solution(object):
    def splitArraySameAverage(self, A):
        if len(A)==1: return False
        global_avg = sum(A)/float(len(A))
        for lenB in range(1, len(A)//2+1):
            if int(lenB*global_avg) == lenB*global_avg:
                if self.exist(lenB*global_avg, lenB, A, 0):
                    return True
        return False
            
    def exist(self, tosum, item_count, arr, idx):
        if item_count==0:
            return False if tosum else True
        if item_count > len(arr) - idx or idx == len(arr): 
            return False
        if any([self.exist(tosum-arr[idx], item_count-1, arr, idx+1),
               self.exist(tosum, item_count, arr, idx+1)]):
            return True
        return False

print(Solution().splitArraySameAverage([5,8,6,7]))