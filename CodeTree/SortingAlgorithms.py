# print result
def print_result(arr):
    for element in arr:
        print(element, end=" ")
    print()

# Bubble Sort
## bubble_original
def bubble_sort(arr):
    for i in range(N - 2):
        for j in range(N - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print_result(arr)

## bubble_upgraded
def bubble_upgraded(arr):
    for i in range(N-2):
        for j in range(N-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print_result(arr)


# Selection Sort
## 내림차순
def selection_sort(arr):
    for i in range(N-1):
        max_idx = i
        for j in range(i+1, N):
            if arr[j] > arr[max_idx]:
                max_idx = j

        arr[i], arr[max_idx] = arr[max_idx], arr[i]
    print_result(arr)

## 오름차순
def selection_reverse(arr):
    for i in range(N-1, 1, -1):
        max_idx = i
        for j in range(i-1, -1, -1):
            if arr[j] > arr[max_idx]:
                max_idx = j

        arr[i], arr[max_idx] = arr[max_idx], arr[i]
    print_result(arr)


# Insertion Sort
def insertion_sort(arr):
    for i in range(1, N):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    print_result(arr)


# Radix Sort
def radix_sort(arr):
    for pos in range(1, 7):
        buckets = [[] for _ in range(10)]
        temp_arr = []
        a = pow(10, pos)
        b = pow(10, pos-1)
        for i in range(N):
            key = (arr[i] % a) // b   # 각 원소[i]별 pos번째 숫자를 구하는 식
            buckets[key].append(arr[i])

        for digit in range(10):
            for element in buckets[digit]:
                temp_arr.append(element)
        arr = temp_arr

    print_result(arr)


# Merge Sort
def merge_sort(arr):
    merged_arr = [0] * N        # N 이것도 전역 변수로 자연스럽게 쓰이고 있는데,
    def divide(low, high):      # 클린 코드는 아닌 듯.
        if low < high:
            mid = (low + high) // 2
            divide(low, mid)
            divide(mid+1, high)
            merge(low, mid, high)

    def merge(low, mid, high):
        i, j = low, mid + 1

        k = low
        while i <= mid and j <= high:
            if arr[i] <= arr[j]:
                merged_arr[k] = arr[i]
                i += 1
                k += 1

            else :
                merged_arr[k] = arr[j]
                j += 1
                k += 1

        while i <= mid:
            merged_arr[k] = arr[i]
            k += 1
            i += 1

        while j <= high:
            merged_arr[k] = arr[j]
            k += 1
            j += 1

        for k in range(low, high + 1):
            arr[k] = merged_arr[k]

    divide(0, N-1)

    print_result(arr)


# Quick Sort
def quick_sort(arr):
    def partition(low, high):
        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[j], arr[i] = arr[i], arr[j]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]

        return i + 1

    def quick(low, high):
        if low < high:
            pos = partition(low, high)

            quick(low, pos - 1)
            quick(pos + 1, high)

    quick(0, N-1)

    print_result(arr)


# Heap Sort
def heap_sort(arr):
    def heapify(n, i):
        largest = i
        l = i * 2
        r = i * 2 + 1

        if l <= n and arr[l] > arr[largest]:
            largest = l

        if r <= n and arr[r] > arr[largest]:
            largest = r

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(n, largest)

    def heap(n):
        for i in range(n//2, -1, -1):
            heapify(n, i)

        for i in range(n, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            heapify(i-1, 0)

    heap(N - 1)
    print_result(arr)
#############################  Main Function  ##################################

N = int(input())
array = list(map(int, input().split()))

# bubble_sort(array)
# bubble_upgraded(array)
# selection_sort(array)
# selection_reverse(array)
# insertion_sort(array)
# radix_sort(array)
# merge_sort(array)
# quick_sort(array)
heap_sort(array)

# 17 21 15 29 81 19 10 35 20


# class화 해보자
