def par(arr,low,high):
    pivot=arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j]<pivot:
            i+=1
            swap(arr,i,j)
    swap(arr,i+1,high)
    return i+1
def swap(arr,i,j):
    arr[i],arr[j]=arr[j],arr[i]
def qs(arr,low,high):
    if low<high:
        pi=par(arr,low,high)
        qs(arr,low,pi-1)
        qs(arr,pi+1,high)
if __name__=="__main__":
    ui=input("Enter the nums: ")
    arr=list(map(int,ui.split()))
    qs(arr,0,len(arr)-1)
    for k in range(len(arr)):
        print(arr[k],end=" ")
        
