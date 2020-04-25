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


def decryption(word, key, dict_alphabet):
    _mod = len(dict_alphabet)
    matrix_list = [[None] * len(word) for i in range(len(key) // len(word))]
    word_list = [dict_alphabet[word[x]] for x in range(len(word))]

    count = 0
    for i in range(len(matrix_list)):
        for j in range(len(matrix_list[0])):
            matrix_list[i][j] = dict_alphabet[key[count]]
            count += 1

    word_array = np.array(matrix_list)
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
    result_list = list()

    for i in range(len(fnl_matrix)):
        sum = 0
        for j in range(len(fnl_matrix[0])):
            sum += (fnl_matrix[i][j] * word_list[j])
            sum = sum % 26

        result_list.append(sum)

    result_letter = list()

    for i in result_list:
        for key in dict_alphabet:
            if dict_alphabet[key] == i:
                result_letter.append(key)

    result = ''.join(result_letter)

    return result

