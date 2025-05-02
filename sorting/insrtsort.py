def ins_sort(arr):
    n=len(arr)
    for i in range(1,n):
        j=i-1
        key=arr[i]
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
            arr[j+1]=key
    for k in range(n):
        print(arr[k],end=" ")
if __name__=="__main__":
    ui=input("enter numsss: ")
    arr=list(map(int,ui.split()))
    ins_sort(arr)
        
