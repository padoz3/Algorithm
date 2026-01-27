import sys

input = sys.stdin.readline
LIST_LEN = 10
TARGET = 7

T = int(input())

def partition(arr, l, r):
    mid = (l + r) // 2
    arr[l], arr[mid] = arr[mid], arr[l]

    pivot = arr[l]

    low = l + 1
    high = r

    while low <= high:
        while low <= high and arr[low] <= pivot: low += 1
        while low <= high and arr[high] >= pivot: high -= 1

        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
            low += 1
            high -= 1
    arr[l], arr[high] = arr[high], arr[l]
    return high

def quick_select(arr, l, h):
    if l < h:
        pivot_idx = partition(arr, l, h)

        if TARGET > pivot_idx:
            quick_select(arr, pivot_idx + 1, h)
        else:
            quick_select(arr, l, pivot_idx - 1)
        
for _ in range(T):
    num_list = list(map(int, input().split()))
    
    quick_select(num_list, 0, LIST_LEN - 1)

    print(num_list[TARGET])