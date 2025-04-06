#!/usr/bin/env python

# edited 2025 for python3

# Assumed usage:
# from dict2 import *
#
# - only some method are redefined - everything else is passed directly to dict
#   see wrapper: __getattr__ !!!


class dict2:
    '''Simple class providing you with dual access:
    a = dict2()
    a.k = 5 is same as  a['k']=5
    and more
    a.update('k1 k2 k3',(1,2,3)) - multi-key access
    a.mget('k1 k2 k3')
    '''

    # ------------------------------------------------------------------------------------
    def _init_from_dict(self, new_keys, from_dict, old_keys):
        if not isinstance(from_dict, dict):
            from_dict = from_dict.__dict__

        if old_keys is None:  # no keys - copy dict
            self.__dict__.update(from_dict)
        else:
            if isinstance(old_keys, str):  # 'k1 ...' -> (k1,k2 ...)
                old_keys = old_keys.split()
            if new_keys is None:  # same keys
                new_keys = old_keys
            if isinstance(new_keys, str):  # 'k1 ...' -> (k1,k2 ...)
                new_keys = new_keys.split()
            for i, j in zip(new_keys, old_keys):
                self.__dict__[i] = from_dict[j]

    # ------------------------------------------------------------------------------------
    def _base_update(self, keys, vals):
        # update dvojic (klice)(values)
        if isinstance(keys,
                      str):  # prevod retezce na klice: 'k1 ...' -> (k1,k2 ...)
            keys = keys.split()
        if isinstance(vals,
                      str):  # prevod retezce na klice: 'k1 ...' -> (k1,k2 ...)
            vals = vals.split()
        self.__dict__.update(zip(keys, vals))

    # ------------------------------------------------------------------------------------
    def __init__(
            self,
            __a=None,
            __b=None,
            __c=None,
            **arg):  # musime __x jinak by se to bylo s x=1 nedal by to do arg
        #print __a,__b,__c
        if isinstance(__a, dict):  # inicializace dict2({2:45, 4:7 ...})
            self.__dict__ = __a
        else:
            self.update(__a, __b, __c)  # vse co umi update
        if arg:  # inicializace jako u dict dict2(a=3,b=5, ...)
            self.__dict__ = arg

    # ------------------------------------------------------------------------------------
    # Possible usage: a-dict2, b-(dict,dict2)
    # a.update({k1:v1,...})
    # a.update(b)                                update from other dict() or dict2()
    #
    # a.update(b,(k1,k2,...)) - i list [k1,...], update from b but only some keys (also as string 'k1 k2 ..')
    # a.update('l1 l2 ...', b, 'k1 k2 ...')      update from b some kays, but key names are changed l1->k1 ...
    #
    # a.update((k1,k2,..), (v1,v2 ...))          update from key -> values
    def update(self, __a, __b=None, __c=None):  # extended syntax for update
        if __a is None and __b is None and __c is None:
            return
        # called as:
        #    update(dict)
        #    update(dict,keys)
        if isinstance(__a, (dict, dict2)):
            self._init_from_dict(None, __a, __b)
        # called as:
        #    update(new_keys,dict, old_keys)
        elif isinstance(__b, (dict, dict2)):
            self._init_from_dict(__a, __b, __c)
        # called as:
        #    update(keys, values) - pouze jeden type volani
        elif __c is None:
            self._base_update(__a, __b)

    # like update but keys are checked for existance,  nonexistent are skipped
    # - be carefull if you really want automaticky skip unexistent keys
    def update2(self, __a, __b, __c=None):
        #    update(dict,keys)
        if isinstance(__a, (dict, dict2)):
            if isinstance(__b, str): __b = __b.split()
            for i in __b:
                if i in __a:
                    self.__dict__[i] = __a[i]  # jen pokud klic existuje

    # vraci tuple(vice) hodnot pro nekolik klicu i default hodnotou
    # x.mget('a b c') - vrati tri hodnoty pro klice a,b,c
    def mget(
            self,
            keys,
            failobj=None):  # musi se jmenovat jinak nez get - vraci vzdy tuple
        if isinstance(keys, str):  # 'k1 ...' -> (k1,k2 ...)
            keys = keys.split()
        vals = []
        for k in keys:
            # if not self.has_key(k):
            if k not in self.__dict__:
                vals.append(failobj)
            else:
                vals.append(self.__dict__[k])
        return tuple(vals)

    def mdel(self, keys):  # remove keys
        if isinstance(keys, str):  # 'k1 ...' -> (k1,k2 ...)
            keys = keys.split()
        for k in keys:
            del self.__dict__[k]

    # ------------------------------------------------------------------------------------
    def dict(self):  # return my : dict
        return self.__dict__

    # metody pro praci s vice poli - nevim jestli je to dobry napad
    # puvodni nazev: def newlists(self, keys) :              # create empty list like: self.k1 = [], ...
    def aslist(self, keys):  # create empty list like: self.k1 = [], ...
        if isinstance(keys, str):  # 'k1 ...' -> (k1,k2 ...)
            keys = keys.split()
        for k in keys:
            self.__dict__[k] = []

    # pro kazdy klic keys proved self.key=dict2()
    def asdict2(self, keys):  # create empty dict2 like: self.k1 = dict2(), ...
        if isinstance(keys, str):  # 'k1 ...' -> (k1,k2 ...)
            keys = keys.split()
        for k in keys:
            self.__dict__[k] = dict2()

    def append(self, keys, values):  # append values to k1, k2, ...
        if isinstance(keys, str):  # 'k1 ...' -> (k1,k2 ...)
            keys = keys.split()
        for k, v in zip(keys, values):
            self.__dict__[k].append(v)

    # get pro pole d[key][idx]
    # x.iget('a b c',0) - vrati trojici prvni hodnota z poli (x.a[0], x.b[0] x.c[0])
    def iget(self, keys,
             idx):  # musi se jmenovat jinak nez get - vraci vzdy tuple
        if isinstance(keys, str):  # 'k1 ...' -> (k1,k2 ...)
            keys = keys.split()
        vals = []
        for k in keys:
            vals.append(self.__dict__[k][idx])
        return tuple(vals)

    # vrati seznam existujicich klicu
    def has(self, keys):
        if isinstance(keys, str):  # 'k1 ...' -> (k1,k2 ...)
            keys = keys.split()
        exist = []
        for k in keys:
            if k in self.__dict__: exist.append(k)
        return exist

    # len(dict2) - return number of keys
    def __len__(self):
        return len(self.__dict__)

    def __delitem__(self, index):
        del self.__dict__[index]

    # a['k'] - getitem
    def __getitem__(self, key):
        return self.__dict__.get(key)

    # a['k'] = 5 - setitem
    def __setitem__(self, key, value):
        self.__dict__[key] = value

    # for iteration over keys: eg for i in a:
    def __iter__(self):
        return self.__dict__.__iter__()

    # def __next__(self):
    #   if self.index >= len(self.__dict__):
    #     raise StopIteration
    #   value = self.__dict__[self.index]
    #   self.index += 1
    #   return value

    # for print
    def __str__(self):
        return str(self.__dict__)

    # def __repr__(self):
    # return "dict2(%s)" % repr(self.__dict__)

    def __getattr__(
            self, name):  # osetri vse co nebylo osetreno - tzv wrapper method
        return getattr(self.__dict__, name)


if __name__ == '__main__':  # pokud to neni modul tak se to spusti
    a = dict2({1: 10, 2: 20, 3: 30})
    print(a)
    print(len(a))  # call __len__
    del a[1]
    print(a.dict())
    print(a[1])  # call __getitem__
    a[9] = 99  # call __setitem__
    print(a)
    a = dict2(a=1, b=2, c=3)
    print(a)
    b = dict2('x y z', (100, 200, 300))
    print(b)
    a.update(b)
    print(a)
    a.update('xxx yyy', b, 'x y')
    print(a)
    if 'c' in a:
        print('c in')

    for i in a:
        print(i, a[i], end=' ')
    print()

    print(a.mget("a b"))  # tuple
    x = a.mget("a")  # tuple
    print(x)
    #  print a["a b"] - not working ? why - we need distinguish between mget('a b') and ['a b']-intentional key='a b'

    # aslist
    c = dict2()
    c.aslist("a1 a2 a3")  # now keys a1,a2,a3 are list: c.a1[i] - dict of lists
    print(c)

    c.append("a1 a2", (1, 2))  # multikey append
    c.append("a1 a2", (3, 4))
    print(c)
    print(c.iget("a1 a2", 1))  # multikey [] - return tuple

    # asdict2
    d = dict2()
    d.asdict2("a b c")  # dict of dicts
    print(d)

    d.a.x = 1
    d.a.y = 1
    d.a.update('u v', (100, 200))
    print(d)

    # d.g.x=1 # to nejde g nebyl deklarovan jako dict
    x = dict2()
    x.update('a b', [1, 2])
    x.update2(c, "a1 a7")
    print(x)
    print(x.has('a b c x'))
    exit(0)
