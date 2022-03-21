def matrix_mult(a, b):
    M_res = []
    for i in range(len(a)):
        new_row = []
        for j in range(len(b[0])):
            new_element = 0
            for k in range(len(a[0])):
                new_element += a[i][k] * b[k][j]
            new_row.append(new_element)
        M_res.append(new_row)
    return M_res


print(matrix_mult(
    [[1, 2],
     [3, 2]],
    #      x
    [[3, 2],
     [1, 1]]
))