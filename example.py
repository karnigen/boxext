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

def check_mget():
    a = str_box("a b c", [1, 2, 3])
    print(f"{mget(a, "a b")=}")

def mset(__a: dict, __keys: (str|list|tuple|dict), __value) -> None:
    if isinstance(__keys, str):
        __keys = __keys.split()
    elif isinstance(__keys, dict):
        __keys = list(__keys.keys())

    for k in __keys:
        __a[k] = __value

def check_mset():
    a = Box()
    print(f"{a=}")
    # mset(a, "a b c", 1)
    mset(a, "a b c", [])
    a.a.append(1)
    print(f"{a=}")

def mlambda(__a: dict, __keys: (str|list|tuple|dict), __values: (str|list|tuple|dict),  __lambda) -> list:
    if isinstance(__keys, str):
        __keys = __keys.split()
    elif isinstance(__keys, dict):
        __keys = list(__keys.keys())

    if isinstance(__values, str):
        __values = __values.split()
    elif isinstance(__values, dict):
        __values = list(__values.values())

    __results = []

    if isinstance(__values, (list, tuple)):
        for i, k in enumerate(__keys):
            __results.append(__lambda(__a, k, __values[i]))
    else:
        for k in __keys:
            __results.append(__lambda(__a, k, __values))
    return __results

def check_mlambda():
    a = Box()
    # d[k] = v
    mset(a, "a b c", [])
    print(f"{a=}")

    # d[k] = v
    # r = mlambda(a, "a b c", [1,2,3], lambda d, k, v: setattr(d, k, [v]))
    # print(f"{a=}, {r=}")

    # d[k].append(v)
    r = mlambda(a, "a b c", [4,5,6], lambda d, k, v: d[k].append(v))
    print(f"{a=}, {r=}")
    r = mlambda(a, "a b c", [7,8,9], lambda d, k, v: d[k].append(v))
    print(f"{a=}, {r=}")

    # d[k][i]
    r = mlambda(a, "a b c", None, lambda d, k, v: d[k][0])
    print(f"{a=}, {r=}")


def main():
    # check_box_from_str()
    # check_update()
    # check_mget()
    # check_mset()
    check_mlambda()

if __name__ == "__main__":
    main()
