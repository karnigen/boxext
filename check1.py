#!/usr/bin/env uvr

from boxext import *

def main():
    a = box_from_str("a b c", "1 2 3")
    a = box_from_str("a b c", [1, 2, 3])
    a = box_from_str("a b c", (1, 2, 3))
    a = box_from_str("a b c", {1: 2, 3: 4, 5: 6})
    a = box_from_str(["a", "b", "c"], {1: 2, 3: 4, 5: 6})
    a = box_from_str({'a':10, 'b':20}, {1: 2, 3: 4})

    # a = box_from_str("a b c", {1: 2, 3: 4})
    print(a)


if __name__ == "__main__":
    main()
