arr=[1,2,3,4,5]
n=len(arr)
temp=[0]*n
for i in range(n):
    temp[i]=arr[n-i-1]
for i in range(n):
    arr[i]=temp[i]
for i in range(n):
    print(arr[i],end=" ")
