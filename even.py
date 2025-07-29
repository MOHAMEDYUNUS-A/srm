import sys
import os

# Add assignment_folder to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'assignment_folder')))

from even_check import is_even

def test_even_cases():
    assert is_even(2)
    assert is_even(4)
    assert is_even(0)

def test_odd_cases():
    assert not is_even(1)
    assert not is_even(3)

if __name__ == "__main__":
    test_even_cases()
    test_odd_cases()
    print("✅ All tests passed!")
