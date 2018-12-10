FILE_NAME = "input.txt.txt"


def read_in_file(file_name):
    with open(file_name, 'r') as input_file:
        result = [line.strip("\n") for line in input_file]

    return result


def count_letters(i_list):
    str_with_2 = 0
    str_with_3 = 0
    for s in i_list:
        d = {}
        for l in s:
            if l not in d:
                d[l] = 0
            d[l] += 1

        got_2 = False
        got_3 = False
        for key, value in d.items():
            if not got_2:
                if value == 2:
                    str_with_2 += 1
                    got_2 = True
            if not got_3:
                if value == 3:
                    str_with_3 += 1
                    got_3 = True
            if got_2 and got_3:
                break

    print("Str count with 2 matching letters: {}".format(str_with_2))
    print("Str count with 3 matching letters: {}".format(str_with_3))
    result = str_with_2 * str_with_3
    return result


def find_similar_strings(i_list):
    for i in range(len(i_list)):
        for j in i_list[(i + 1):]:
            diff_no = 0
            str_a = i_list[i]
            str_b = j

            # Both words same length
            for c in range(len(str_a)):
                if str_a[c] != str_b[c]:
                    diff_no += 1
                if diff_no > 1:
                    break

            if diff_no < 2:
                print("Similar words: {} - {}".format(str_a, str_b))
                return str_a, str_b


def get_word_similarity(str_a, str_b):
    result = ""
    for i in range(len(str_a)):
        if str_a[i] == str_b[i]:
            result += str_a[i]
    return result


if __name__ == '__main__':
    input_list = read_in_file(FILE_NAME)
    letter_counts = count_letters(input_list)
    print("Multiplication result: {}".format(letter_counts))

    similar_words = find_similar_strings(input_list)
    similar_word = get_word_similarity(similar_words[0], similar_words[1])
    print("Similar word: {}".format(similar_word))
