
# pytest
import pytest

# BoxExt
from boxext import *

def test_update():
    # Test with string keys and values
    a = str_box("a b c", "1 2 3")
    update_pairs(a, "b c", "4 5")
    assert a.a == "1"
    assert a.b == "4"
    assert a.c == "5"
    assert len(a) == 3
    assert a == {'a': '1', 'b': '4', 'c': '5'}
    assert isinstance(a, Box)
    assert isinstance(a, dict)

    # Test nonexistent keys
    a.update({"d": "6"})
    assert a.d == "6"
    assert len(a) == 4
    assert a == {'a': '1', 'b': '4', 'c': '5', 'd': '6'}
