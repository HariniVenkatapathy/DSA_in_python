def conseq(arr):
    arr.sort()
    count = 0
    j = 1
    i = 0
    while len(arr)+1:
        if arr[i] + 1 == arr[j]:
            count += 1
        else:
            break 
        
        i += 1
        j += 1
    print(count+1)

if __name__ == "__main__":
    arr = list(map(int,input().split()))
    conseq(arr)
