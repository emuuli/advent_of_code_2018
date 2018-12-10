FILE_NAME = "input.txt.txt"


def read_in_file(file_name):
    with open(file_name, 'r') as input_file:
        result = [int(line) for line in input_file]

    return result


def find_first_duplicate(i_list):
    results = set()
    current_result = 0
    results.add(current_result)

    while True:
        for i in i_list:
            current_result += i
            if current_result in results:
                return current_result
            else:
                results.add(current_result)


if __name__ == '__main__':
    input_list = read_in_file(FILE_NAME)
    input_list_sum = sum(input_list)
    print("Sum of input.txt list: {}".format(input_list_sum))

    first_duplicate = find_first_duplicate(input_list)
    print("First duplicate: {}".format(first_duplicate))
