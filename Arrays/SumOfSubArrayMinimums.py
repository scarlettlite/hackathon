class Solution(object):
    def sumSubarrayMins(self, A):
        MOD = 10**9 + 7

        stack = []
        ans = dot = 0
        for y in A:
            count = 1
            while stack and stack[-1][0] > y:
                x,c = stack.pop()
                count += c
                dot -= c * x
            stack.append((y, count))
            dot += y * count
            ans += dot

        return dot

print(Solution().sumSubarrayMins([1,7,5,2,4,3,9]))