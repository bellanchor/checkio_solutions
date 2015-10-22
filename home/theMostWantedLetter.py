# -*- coding: utf-8 -*-
'''
http://www.checkio.org/mission/most-wanted-letter/
'''

import string
import time

def tt(f):
    def wrapper(text):
        start = time.clock()
        for i in range(100000):
            ret = f(text)
        end = time.clock()
        print end-start
        return ret

    return wrapper


@tt
def checkio(text):
    text = text.lower()
    textlist = ''.join(text.split())
    textlist = [ t for t in textlist if t.isalpha() ]
    textlist.sort(reverse=True)

    mostWanted = alp = textlist.pop()
    num = 1
    numsave = 0
    while len(textlist):
        p = textlist.pop()
        if alp == p:
            num += 1
        else:
            if num > numsave:
                numsave = num
                mostWanted = alp
            num = 1
            alp = p

    return mostWanted

@tt
def shorter_solution(text):
    return max(string.ascii_lowercase, key=lambda ch: text.lower().count(ch))

a = 'abc fjks 123111111ffff a a bbbb!'
print checkio(a)
print shorter_solution(a)
