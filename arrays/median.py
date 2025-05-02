def median(arr1,arr2):
    arr3=arr1+arr2
    n=len(arr3)
    for i in range(n-1):
        minidx=i
        for j in range(i+1,n):
            if arr3[j]<arr3[minidx]:
                min_idx=j
        arr3[j],arr3[minidx]=arr3[minidx],arr3[j]
        if n%2==0:
            temp=n//2
            mid=temp-1
            median=((arr3[temp]+arr3[mid]/2))
            if median.is_integer():
                return Int(median)
            return median
        else:
            return arr3[n//2]
if __name__=="__main__":
    arr1 = [-5, 3, 6, 12, 15]
    arr2 = [-12, -10, -6, -3, 4, 10]
    print(median(arr1,arr2))
                
