# [ 5, 6, 1, 3, 5, 6, 4, 3, 12, 81]

def getLCISLength(arr):
   # print len(arr)
    max_length = 1;
    curr_length = 1;
    if(len(arr) == 0):
        return 0
    if(len(arr) == 1):
        return 1
    for i in range(1, len(arr)):
        if(arr[i-1] < arr[i]):
            curr_length += 1
        else:
            if(max_length < curr_length):
                #print "curr_length" + str(curr_length)
                max_length = curr_length
                curr_length = 1

    if(max_length < curr_length):
        max_length = curr_length

    #print "max_length" + str(max_length)

    return max_length
        

def main():
    getLCISLength([ 5, 6, 1, 3, 5, 6, 4, 3, 12, 81, 100, 120] )

main()