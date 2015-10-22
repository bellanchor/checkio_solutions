# -*- coding: utf-8 -*-
'''
http://www.checkio.org/mission/x-o-referee/
'''

def checkio(a):
    for i in range(3):
        if a[i].count("X") == 3 or a[i].count("O") == 3:
            return a[i][0]
        
        if a[0][i] == a[1][i] == a[2][i] != ".":
            return a[0][i]

    if a[0][0] == a[1][1] == a[2][2] != "." or a[0][2] == a[1][1] == a[2][0] != ".":
        return a[1][1]

    return "D"

if __name__ == '__main__':
    assert checkio([
        u"X.O",
        u"XX.",
        u"XOO"]) == "X", "Xs wins"
    assert checkio([
        u"OO.",
        u"XOX",
        u"XOX"]) == "O", "Os wins"
    assert checkio([
        u"OOX",
        u"XXO",
        u"OXX"]) == "D", "Draw"
