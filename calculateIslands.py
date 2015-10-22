# -*- coding: utf-8 -*-
'''
http://www.checkio.org/mission/calculate-islands/
'''

def checkio(data):
    rows = len(data)
    cols = len(data[0])
    
    visited = [[0 for i in range(cols)] for j in range(rows)]
    
    area = []
        
    for j in range(rows):
        for i in range(cols):
            if visited[j][i]:
                continue
                
            if data[j][i]:
                area.append(0)
                visited[j][i] = 1
                visited, area[-1] = lookfor(data, j, i, visited, area[-1], rows, cols)
            else:
                visited[j][i] = 1
    
    
    #sort in ascending order

    return area and sorted(area)

def lookfor(data, row, col, visited, area, rows, cols):
    area += 1

    for j in range(-1,2):
        for i in range(-1,2):
            new_row = row + j
            new_col = col + i
            if rows > new_row >= 0 and cols > new_col >= 0:
                if not visited[new_row][new_col]:
                    visited[new_row][new_col] = 1
                    if data[new_row][new_col]:
                        visited, area = lookfor(data, new_row, new_col, visited, area, rows, cols)
    
    return visited, area

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([[0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 0],
                    [0, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0]]) == [1, 3], "1st example"
    assert checkio([[0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 0],
                    [0, 1, 1, 0, 0]]) == [5], "2nd example"
    assert checkio([[0, 0, 0, 0, 0, 0],
                    [1, 0, 0, 1, 1, 1],
                    [1, 0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 1, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0]]) == [2, 3, 3, 4], "3rd example"

