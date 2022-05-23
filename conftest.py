import random

import pytest


@pytest.fixture
def one_element_array():
    return [1]


@pytest.fixture
def empty_array():
    return []


@pytest.fixture
def unsorted_2_element_array():
    return [2, 1]


@pytest.fixture
def sorted_2_element_array():
    return [1, 2]


@pytest.fixture
def reversed_array_10():
    return [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


@pytest.fixture
def unsorted_array_10():
    return [1, 3, 4, 5, 2, 10, 8, 7, 9, 6]


@pytest.fixture
def sorted_array_10():
    return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


@pytest.fixture
def reversed_array_1000():
    arr = []
    for x in range(1000, 0, -1):
        arr.append(x)
    return arr


@pytest.fixture
def random_array_1000():
    arr = [i + 1 for i in range(1000)]
    result = []
    while len(arr) > 0:
        idx = random.randint(0, len(arr) - 1)
        result.append(arr.pop(idx))
    return result


@pytest.fixture
def sorted_array_1000():
    arr = [i + 1 for i in range(1000)]
    return arr
