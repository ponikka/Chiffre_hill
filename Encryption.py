def encryption(word, key, dict_alphabet):
    matrix_list = [[None] * len(word) for i in range(len(key) // len(word))]
    word_list = [dict_alphabet[word[x]] for x in range(len(word))]

    count = 0
    for i in range(len(matrix_list)):
        for j in range(len(matrix_list[0])):
            matrix_list[i][j] = dict_alphabet[key[count]]
            count += 1

    result_list = list()

    for i in range(len(matrix_list)):
        sum = 0
        for j in range(len(matrix_list[0])):
            sum += (matrix_list[i][j] * word_list[j])
            sum = sum % 26

        result_list.append(sum)

    result_letter = list()

    for i in result_list:
        for key in dict_alphabet:
            if dict_alphabet[key] == i:
                result_letter.append(key)

    result = ''.join(result_letter)
    return result
