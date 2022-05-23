from math import floor


def mergeSort(arr: list[int]):
    # BASE CASE: arr is len <=1 means sorted
    n = len(arr)
    if n <= 1:
        return arr
    # merge sort left side
    left = mergeSort(arr[0 : floor(n / 2)])
    # merge sort right side
    right = mergeSort(arr[floor(n / 2) :])
    # merge left and right
    return merge_lists(left, right)


def merge_lists(left: list[int], right: list[int]):
    # initialize resulting array
    result = []
    left_n = len(left)
    right_n = len(right)
    left_idx = 0
    right_idx = 0
    # while there are vals left to merg ein both left and right
    while left_idx < left_n and right_idx < right_n:
        # if cur lef tis less than cur_right add left
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        # else add right
        else:
            result.append(right[right_idx])
            right_idx += 1
    # if no more on left side add rest of right
    if left_idx >= left_n:
        result += right[right_idx:]
    # if no more on right side add rest of left
    elif right_idx >= right_n:
        result += left[left_idx:]
    return result
