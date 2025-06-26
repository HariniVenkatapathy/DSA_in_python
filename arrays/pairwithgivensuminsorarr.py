def pairofsorarr(target,arr):
    count = 0
    for i in range(len(arr)):
        for j in range(i+1,len(arr),1):
            temp = arr[i]+arr[j]
            if temp == target:
                count += 1
    print(count)

if __name__ == "__main__":
    target = int(input())
    arr = list(map(int,input().split()))
    pairofsorarr(target,arr)

    
        
