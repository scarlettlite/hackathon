#2, 7, 3, 6
#7, 6, 3, 2

def maxSwap(num):
    arr = []
    while(num != 0):
        digit = num % 10
        arr.append(digit)
        num = num /10
    
    #what is more efficient ? creating a list by copying or appending
    #mistake 1
    sortedArr = list(arr)
    arr.reverse()
    sortedArr.sort(reverse=True)
    for i in range(0, len(arr)):
        if(sortedArr[i] > arr[i]):
            #mistake2
            temp = arr[i]
            index = arr.index(sortedArr[i])
            arr[i] = sortedArr[i]
            arr[index] = temp
            break
    result = 0
    for i in range(0, len(arr)):
        result = (result * 10) + arr[i]

    return result

def main():
    print maxSwap(2736)
    print maxSwap(9973)
    print maxSwap(1234)
    print maxSwap(2244)
    print maxSwap(35357811)


main()





