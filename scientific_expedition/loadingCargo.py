# -*- coding: utf-8 -*-
'''
http://www.checkio.org/mission/loading-cargo/
'''

def checkio(data):
    
    datain = [data]
    
    res = getAllPosRes(datain)
    
    if isinstance(res, list):
        return min(res)
    elif isinstance(res, int):
        return res
    
def getAllPosRes(datain):
    '''
    datain should be some lists in a list, eg [[]], [[1,2], [2,3]] ...
    '''

    allPosRes = []

    #print datain
    endFlag = False

    for data in datain:
    
        if len(data) == 0: return 0
    
        if len(data) == 1: return data

        if len(data) == 2: 
            allPosRes.append(abs(data[0] - data[1]))
            endFlag = True
            continue
        
        datacopy = data[:]
    
        datamax1 = max(datacopy)
    
        datacopy.remove(datamax1)
        
        if datamax1 >= sum(datacopy):
            symbol = [-1]
        else:
            symbol = [1, -1]
            
        datamax2 = max(datacopy)
        
        datacopy.remove(datamax2)
        
        for i in symbol:
            
            tmp = datamax1 + i * datamax2
            
            allPosRes.append(datacopy + [tmp])
    
        
    if endFlag:
        return allPosRes
    else:
        allPosRes = getAllPosRes(allPosRes)
        return allPosRes

if __name__ == '__main__':
    assert checkio([10, 10]) == 0, "1st example"
    assert checkio([10]) == 10, "2nd example"
    assert checkio([5, 8, 13, 27, 14]) == 3, "3rd example"
    assert checkio([5, 5, 6, 5]) == 1, "4th example"
    assert checkio([12, 30, 30, 32, 42, 49]) == 9, "5th example"
    assert checkio([1, 1, 1, 3]) == 0, "6th example"

