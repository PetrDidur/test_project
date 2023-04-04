from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"
    assert arrs.get([1, 5, 3], 1, "test") == 5
    assert arrs.get([1, 2, 3], -1, "test") == "test"
    assert arrs.get([1, 2, 3], 2, "test") == 3
    assert arrs.get([1, 2, 3], 4, "not found") == "not found"



def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([], 1, 2) == []
    assert arrs.my_slice([1, 2, 3], -1) == [3]
    assert arrs.my_slice([1, 2, 3, 4], 1, -1) == [2, 3]
    assert arrs.my_slice([1, 2, 3, 4], -1, 1) == []
    assert arrs.my_slice([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert arrs.my_slice([1, 2, 3, 4, 5], 2) == [3, 4, 5]
    assert arrs.my_slice([1, 2, 3, 4, 5], -3, -1) == [3, 4]
    assert arrs.my_slice([1, 2, 3, 4, 5], end=3) == [1, 2, 3]
    assert arrs.my_slice([1, 2, 3, 4], end=-3) == [1]
    assert arrs.my_slice([1, 2, 3, 4], -5, 2) == [1, 2]