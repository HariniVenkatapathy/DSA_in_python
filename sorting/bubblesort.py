def bubb_sort(arr):
    n=len(arr)
    for i in range(n):
        swapped= False
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
        if (swapped==False):
            break
    for k in range(n):
        print(arr[k],end=" ")
if __name__=="__main__":
    ui=input("enter numey: ")
    arr=list(map(int,ui.split()))
    bubb_sort(arr)
            
