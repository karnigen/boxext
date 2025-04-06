#!/usr/bin/env uvr

from boxext import *


def check_box_from_str():
    print(f"{str_box("a b c", "1 2 3")=}")
    print(f"{str_box("a b c", [1, 2, 3])=}")
    print(f"{str_box("a b c", (1, 2, 3))=}")
    print(f"{str_box("a b c", {1: 2, 3: 4, 5: 6})=}")
    print(f"{str_box(["a", "b", "c"], {1: 2, 3: 4, 5: 6})=}")
    print(f"{str_box({'a':10, 'b':20}, {1: 2, 3: 4})=}")
    print(f"{Box(['a','b'],[1,2])=}")


def check_update():
    a = str_dict("a b c", "1 2 3")
    # a.update(Box({"b": 4, "c": 5}))
    a.update(str_box("b c", "4 5"))
    print(f"{a=}")



def main():
    # check_box_from_str()
    check_update()

if __name__ == "__main__":
    main()
