# coding: utf-8
def zero_row(matrix, index):
    matrix[index] = [0 for _ in range(len(matrix))]
    
def zero_column(matrix, index):
    for i in range(len(matrix)):
        matrix[i][index] = 0
        
def zero_matrix(matrix):
    m = len(matrix)
    n = len(matrix[0])
    row = [False for _ in range(m)]
    col = [False for _ in range(n)]
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                row[i] = True
                col[j] = True
    for i in range(m):
        if row[i]:
            zero_row(matrix, i)
    for j in range(n):
        if col[j]:
            zero_column(matrix, j)
            
