# -*- coding:utf-8 -*-
'''
http://www.checkio.org/mission/roman-numerals/
'''

def checkio(a):
    if a < 1:
        print 'invalid input'
    else:
        a = int(a)

    rel = {1:'I', 
           5:'V',
           10:'X',
           50:'L',
           100:'C',
           500:'D',
           1000:'M'}
    
    rom = ''

    rel_keys = sorted(rel.keys(), reverse=True)

    for i in range(len(rel_keys)):

        q = a / rel_keys[i]

        if q != 0:

            add_10npower = 10**(len(str(rel_keys[i]))-1)

            qq = (a + add_10npower) / rel_keys[i-1] if i > 0 else 0

            if qq != 0:
                rom += (rel[add_10npower] + rel[rel_keys[i-1]])
                r = (a + add_10npower) % rel_keys[i-1]
            else:
                rom += rel[rel_keys[i]] * q
                r = a % rel_keys[i]

            if r == 0:
                break

            a = r

    return rom

print checkio(6)
print checkio(76)
print checkio(499)
print checkio(3888)
