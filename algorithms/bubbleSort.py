from shared.helper_functions import swap_vals


def bubbleSort(arr: list[int]):
    # Swap sequential values until full list is sorted
    n = len(arr)
    for i in range(1, n):
        swapped = False
        for j in range(0, n - i):
            if arr[j] > arr[j + 1]:
                swap_vals(arr, j, j + 1)
                swapped = True
        if not swapped:
            # If no swapping happened than arr is sorted
            return
