

def calculateRangeSum(arr):
    rangeSum = [0] * len(arr)
    if(len(arr) == 0):
        return rangeSum
    rangeSum[0] = arr[0]
    if(len(arr) == 1):
        return rangeSum
    for i in range(1, len(arr)):
        rangeSum[i] = rangeSum[i - 1] + arr[i]
    return rangeSum

def getRangeSum(rangeSums, i, j):
    if(i <= j and j < len(rangeSums)):
        if(i == 0):
            return rangeSums[j]
        else:
            return rangeSums[j] - rangeSums[i-1]

def main():
    rangeSums = calculateRangeSum([-2, 0, 3, -5, 2, -1])
    print(getRangeSum(rangeSums, 0, 2))
    print(getRangeSum(rangeSums, 2, 5))
    print(getRangeSum(rangeSums, 0, 5))

main()

