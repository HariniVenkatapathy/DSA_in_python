def maxindexarr(arr): #wrong code
    maxiindex = 0
    temp = 0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]<arr[j]and i<j:
                temp = j-i
            if temp>maxiindex:
                maxiindex = temp
    print(maxiindex)
                

if __name__ == "__main__":
    arr = list(map(int,input().split()))
    maxindexarr(arr)
