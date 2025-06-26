def arrayleaders(arr):
    n = len(arr)
    a = []
    max_from_right = arr[-1]  # The last element is always a leader
    a.append(max_from_right)
    for i in range(n - 2, -1, -1):
        if arr[i] >= max_from_right:
            a.append(arr[i])
            max_from_right = arr[i]

    # Since we went from right to left, reverse to print in original order
    a.reverse()
    print(a)

if __name__ == "__main__":
    arr = list(map(int,input().split()))
    arrayleaders(arr)
