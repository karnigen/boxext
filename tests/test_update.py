
# pytest
import pytest

# BoxExt
from boxext import *

def test_update_pairs():
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


def test_update_selected():
    # Test with string keys
    a = str_box("a b c", "1 2 3")
    b = str_box("b c d", "4 5 6")
    update_selected(a, b, "b c")
    assert a.a == "1"
    assert a.b == "4"
    assert a.c == "5"
    assert len(a) == 3
    assert a == {'a': '1', 'b': '4', 'c': '5'}
    assert isinstance(a, Box)
    assert isinstance(a, dict)

    # Test nonexistent keys
    a = str_box("a b c d", "1 2 3 4")
    b = str_box("b c d", "4 5 6")
    update_selected(a, b, a)
    assert a.d == "6"

def test_mget():
    a = str_box("a b c", [1, 2, 3])
    assert mget(a, "a b") == (1, 2)
    assert mget(a, "a") == (1,)
    assert mget(a, "b") == (2,)
    assert mget(a, "c") == (3,)
    assert mget(a, "d") == ()
    assert mget(a, "a d") == (1,)
    assert mget(a, "a b d") == (1, 2)
    assert mget(a, "a b c") == (1, 2, 3)

    a = str_box("a b c", [1, 2, 3])
    b = str_box("b c d", [4, 5, 6])
    assert mget(a, b) == (2, 3)

def test_mdel():
    a = str_box("a b c", [1, 2, 3])
    assert mdel(a, "a b") == ['a', 'b']
    assert len(a) == 1
    assert a == {'c': 3}
    assert isinstance(a, Box)
    assert isinstance(a, dict)

    a = str_box("a b c d", [1, 2, 3, 4])
    b = str_box("b c d", [4, 5, 6])
    assert mdel(a, b) == ['b', 'c', 'd']
    assert len(a) == 1
    assert a == {'a': 1}
    assert isinstance(a, Box)
    assert isinstance(a, dict)