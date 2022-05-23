from algorithms.bubbleSort import bubbleSort


def test_one_element(one_element_array):
    bubbleSort(one_element_array)
    assert one_element_array == one_element_array


def test_empty_array(empty_array):
    bubbleSort(empty_array)
    assert empty_array == empty_array


def test_2_element_array(unsorted_2_element_array, sorted_2_element_array):
    bubbleSort(unsorted_2_element_array)
    assert unsorted_2_element_array == sorted_2_element_array


def test_array_10(reversed_array_10, unsorted_array_10, sorted_array_10):
    bubbleSort(reversed_array_10)
    assert reversed_array_10 == sorted_array_10
    bubbleSort(unsorted_array_10)
    assert unsorted_array_10 == sorted_array_10


def test_array_1000(reversed_array_1000, random_array_1000, sorted_array_1000):
    bubbleSort(reversed_array_1000)
    assert reversed_array_1000 == sorted_array_1000
    bubbleSort(random_array_1000)
    assert random_array_1000 == sorted_array_1000
