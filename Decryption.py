import numpy as np


def create_the_matrix(matrix, factor_2):
    main_matrix = []
    for i in matrix:
        elem = []
        for j in i:
            number = ((int(round(j * factor_2))))
            elem.append(number)
        main_matrix.append(elem)

    return main_matrix


def matrix_of_mod(matrix, _mod):
    final_matrix = []
    for i in matrix:
        result_matrix = []
        for j in i:
            if j < 0:
                element = abs(j) % _mod
                element *= -1
                result_matrix.append(element)
            else:
                element = j % _mod
                result_matrix.append((element))
        final_matrix.append(result_matrix)
    return final_matrix


def bezout(a, b):
    x, xx, y, yy = 1, 0, 0, 1
    while b:
        q = a // b
        a, b = b, a % b
        x, xx = xx, x - xx * q
        y, yy = yy, y - yy * q
    return x


def create_finall_matrix(matrix, _mod):
    fnl_matrix = []
    for i in matrix:
        res_matrix = []
        for j in i:
            if j < 0:
                res_matrix.append(_mod + j)
            else:
                res_matrix.append(j)
        fnl_matrix.append(res_matrix)

    return fnl_matrix


def decryption(word, _mod):
    word_array = np.array(word)
    inv_matrix = np.linalg.inv(word_array)
    det = int(np.linalg.det(word_array))
    main_matrix = create_the_matrix(inv_matrix, det)
    transpose_matrix = np.array(main_matrix)
    transpose_matrix = np.matrix.transpose(transpose_matrix)
    final_matrix = matrix_of_mod(transpose_matrix, _mod)

    x = bezout(det, _mod)

    if det > 0 and x > 0:
        x = x
    elif det < 0 and x < 0:
        x = x * -1
    elif det > 0 and x < 0:
        x = _mod + x
    elif det < 0 and x > 0:
        x = x

    result_matrix = create_the_matrix(final_matrix, x)
    result_matrix = matrix_of_mod(result_matrix, _mod)

    r_m = np.array(result_matrix)
    r_m = np.matrix.transpose(r_m)

    fnl_matrix = create_finall_matrix(r_m, _mod)
    return fnl_matrix

