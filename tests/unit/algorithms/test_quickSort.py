# import sys

from algorithms.quickSort import quickSort


def test_one_element(one_element_array):
    quickSort(one_element_array)
    assert one_element_array == one_element_array


def test_empty_array(empty_array):
    quickSort(empty_array)
    assert empty_array == empty_array


def test_2_element_array(unsorted_2_element_array, sorted_2_element_array):
    quickSort(unsorted_2_element_array)
    assert unsorted_2_element_array == sorted_2_element_array


def test_array_10(reversed_array_10, unsorted_array_10, sorted_array_10):
    quickSort(reversed_array_10)
    assert reversed_array_10 == sorted_array_10
    quickSort(unsorted_array_10)
    assert unsorted_array_10 == sorted_array_10


def test_array_1000(reversed_array_1000, random_array_1000, sorted_array_1000):
    quickSort(reversed_array_1000)
    assert reversed_array_1000 == sorted_array_1000
    quickSort(random_array_1000)
    assert random_array_1000 == sorted_array_1000
