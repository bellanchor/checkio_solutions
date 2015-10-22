# -*- coding: utf-8 -*-
'''
http://www.checkio.org/mission/min-max/
'''

def check_iter(*args):
    alen = len(args)
    if alen == 1:
        args = args[0]
        if not (hasattr(args, "__iter__") or hasattr(args, "__getitem__")):
            raise ValueError, "the parameter is not acceptable: %s" %args
    return args

def get_cmp_tools(lead_item, method, func):
    if hasattr(func(lead_item), '__cmp__'):
        cmpattr = '__cmp__'
    else:
        cmpattr = None

    if method == 'max':
        if not cmpattr and hasattr(func(lead_item), "__gt__"):
            cmpattr = "__gt__"
        take = 1
    elif method == 'min':
        if not cmpattr and hasattr(func(lead_item), "__lt__"):
            cmpattr = "__lt__"
            take = 1
        else:
            take = -1

    return cmpattr, take

def get_first(*args):
    if len(args) == 1:
        try:
            return args[0][0], 0
        except TypeError:
            if hasattr(args[0], "next"):
                return args[0].next(), 1
            elif hasattr(args[0], "pop"):
                return args[0].pop(), 2
    else:
        return args[0], 0

def maxmin(*args, **kwargs):
    args = check_iter(*args)

    if "key" in kwargs:
        func = kwargs["key"]
    else:
        func = lambda x: x

    lead_item, gen = get_first(args)
    method = kwargs["method"]

    cmpattr, take = get_cmp_tools(lead_item, method, func)

    if gen == 1:
        cur = args.next()
        while True:
            if getattr(func(cur), cmpattr)(func(lead_item)) == take:
                lead_item = cur
            try:
                cur = args.next()
            except StopIteration:
                break
    elif gen == 2:
        cur = args.pop()
        while True:
            if getattr(func(cur), cmpattr)(func(lead_item)) == take:
                lead_item = cur
            try:
                cur = args.pop()
            except KeyError:
                break
    else:
        for cur in args[1:]:
            if getattr(func(cur), cmpattr)(func(lead_item)) == take:
                lead_item = cur

    return lead_item



def max(*args, **kwargs):
    kwargs["method"] = "max"
    return maxmin(*args, **kwargs)

def min(*args, **kwargs):
    kwargs["method"] = "min"
    return maxmin(*args, **kwargs)

if __name__ == '__main__':

    assert(max(3, 2) == 3)
    assert(min(3, 2) == 2)
    assert(max([1,2,0,3,4]) == 4)
    assert(min("hello")) == "e"
    assert(max(2.2, 5.6, 5.9, key=int)) == 5.6
    assert(min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0])
    assert(min(abs(i) for i in range(-10, 10)) == 0)
    assert(min({1,2,3,4}) == 1)
