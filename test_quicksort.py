import sys
import os

# Add 'assignment_folder' to sys.path so we can import quicksort.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'assignment_folder')))

from quicksort import quicksort

def test_quicksort():
    assert quicksort([3, 2, 1]) == [1, 2, 3]
    assert quicksort([5, 3, 8, 4, 2]) == [2, 3, 4, 5, 8]
    assert quicksort([]) == []
    assert quicksort([1]) == [1]
    assert quicksort([9, 9, 9]) == [9, 9, 9]
    assert quicksort([2, 1, 3, 1]) == [1, 1, 2, 3]
    assert quicksort([-3, -1, -2, 0]) == [-3, -2, -1, 0]
    assert quicksort([100, 20, 30, 10]) == [10, 20, 30, 100]

if __name__ == "__main__":
    test_quicksort()
    print("✅ All quicksort tests passed!")
