def removedupli(arr):
    n = len(arr)
    while n>0: #optimize this
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if arr[i] == arr[j]:
                    arr.remove(arr[j])
                    break
        n -= 1
        
    print(arr)

if __name__ == "__main__":
    arr = list(map(int,input().split()))
    removedupli(arr)
    
