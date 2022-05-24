import random

from shared.helper_functions import swap_vals


def quickSort(arr: list[int]):
    # call recursive with start and end
    quickSortRec(arr, 0, len(arr) - 1)


def quickSortRec(arr: list[int], start: int, end: int):
    # randomly select pivot point. make all points less than pivot on left, all greater than on right
    # BASE CASE : start index is greater than end index
    if start > end:
        return
    # Get pivot index
    pivot = partition(arr, start, end)
    # quick Sort both sides of pivot
    quickSortRec(arr, start, pivot - 1)
    quickSortRec(arr, pivot + 1, end)


def partition(arr: list[int], start: int, end: int):
    # select random pivot
    pivotIdx = random.randint(start, end)
    # move point to end of array
    swap_vals(arr, pivotIdx, end)
    pivotVal = arr[end]
    # set last swapped to start
    lastSwapped = start - 1
    # traverse through all elements except for pivot
    for i in range(start, end):
        # if value is less than pivot
        if arr[i] <= pivotVal:
            # increment last swapped and swap val with val after last swapped
            lastSwapped += 1
            swap_vals(arr, i, lastSwapped)
    # pivot point is element after last swapped
    pivotPoint = lastSwapped + 1
    swap_vals(arr, pivotPoint, end)
    return pivotPoint
