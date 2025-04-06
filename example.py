#!/usr/bin/env uvr

from boxext import *


def check_box_from_str():
    print(f"{box_from_str("a b c", "1 2 3")=}")
    print(f"{box_from_str("a b c", [1, 2, 3])=}")
    print(f"{box_from_str("a b c", (1, 2, 3))=}")
    print(f"{box_from_str("a b c", {1: 2, 3: 4, 5: 6})=}")
    print(f"{box_from_str(["a", "b", "c"], {1: 2, 3: 4, 5: 6})=}")
    print(f"{box_from_str({'a':10, 'b':20}, {1: 2, 3: 4})=}")
    print(f"{Box(['a','b'],[1,2])=}")


def check_update():
    pass



def main():
    check_box_from_str()

if __name__ == "__main__":
    main()
