from shared.helper_functions import swap_vals


def selectionSort(arr: list[int]):
    # find lowest in unsorted part of array and add it the end of sorted part of the array
    n = len(arr)
    for i in range(0, n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        swap_vals(arr, i, min_idx)
