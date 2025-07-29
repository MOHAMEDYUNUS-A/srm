
from quicksort import quicksort

def test_quicksort_sorted():
    assert quicksort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_quicksort_unsorted():
    assert quicksort([5, 2, 1, 4, 3]) == [1, 2, 3, 4, 5]

def test_quicksort_duplicates():
    assert quicksort([3, 3, 2, 1, 2]) == [1, 2, 2, 3, 3]

def test_quicksort_empty():
    assert quicksort([]) == []

def test_quicksort_single():
    assert quicksort([7]) == [7]
