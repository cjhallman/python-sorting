from algorithms.mergeSort import mergeSort


def test_one_element(one_element_array):
    result = mergeSort(one_element_array)
    assert result == one_element_array


def test_empty_array(empty_array):
    result = mergeSort(empty_array)
    assert result == empty_array


def test_2_element_array(unsorted_2_element_array, sorted_2_element_array):
    result = mergeSort(unsorted_2_element_array)
    assert result == sorted_2_element_array


def test_array_10(reversed_array_10, unsorted_array_10, sorted_array_10):
    result = mergeSort(reversed_array_10)
    assert result == sorted_array_10
    result = mergeSort(unsorted_array_10)
    assert result == sorted_array_10


def test_array_1000(reversed_array_1000, random_array_1000, sorted_array_1000):
    result = mergeSort(reversed_array_1000)
    assert result == sorted_array_1000
    result = mergeSort(random_array_1000)
    assert result == sorted_array_1000
