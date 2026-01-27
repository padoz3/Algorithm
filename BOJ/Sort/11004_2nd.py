import sys
input = sys.stdin.readline

def partition(arr, l, r):
    mid = (l + r) // 2 
    arr[l], arr[mid] = arr[mid], arr[l] 

    pivot = arr[l]
    low = l + 1
    
    while low <= r:
        while low <= r and arr[low] < pivot: low += 1
        
        while r >= low and arr[r] > pivot: r -= 1 

        if low <= r:
            arr[low], arr[r] = arr[r], arr[low]
            low += 1
            r -= 1

    arr[l], arr[r] = arr[r], arr[l]
    return r

def quick_select(arr, left, right, k):
    if left < right:
        pivot_idx = partition(arr, left, right)

        if pivot_idx == k:
            return
        elif k < pivot_idx:
            quick_select(arr, left, pivot_idx - 1, k)
        else:
            quick_select(arr, pivot_idx + 1, right, k)

N, K = map(int, input().split())
num_list = list(map(int, input().split()))

quick_select(num_list, 0, N - 1, K - 1)

print(num_list[K - 1])