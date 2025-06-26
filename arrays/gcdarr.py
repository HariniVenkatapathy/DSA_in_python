import math

def gcdarray(n, arr):
    result = arr[0]
    for i in range(1, n):
        result = math.gcd(result, arr[i])
    return result

if __name__ == "__main__":
    N = int(input("Enter number of elements: "))
    arr = list(map(int, input("Enter elements: ").split()))
    print("GCD of array:", gcdarray(N, arr))

