import re

FILE_NAME = "input.txt"
initial_state = '###....#..#..#......####.#..##..#..###......##.##..#...#.##.###.##.###.....#.###..#.#.##.#..#.#'


def extract_ints(a_string):
    return tuple(map(int, re.findall(r'-?\d+', a_string)))


def read_in_file(file_name):
    result = []
    with open(file_name, 'r') as input_file:
        for line in input_file:
            d = {}
            parts = line.strip("[\n").split(" => ")
            d[parts[0]] = parts[1]

            result.append(d)

    return result


if __name__ == '__main__':
    rules = read_in_file(FILE_NAME)
    starting_point = 0

    for gen in range(20):
        initial_state = "...." + initial_state + "...."
        starting_point += 4
        new_state = ""
        for i in range(len(initial_state)):
            current_state = initial_state[i:i + 5]
            rule_found = False
            for rule in rules:
                if current_state in rule:
                    new_state += rule[current_state]
                    rule_found = True
                    break
            if not rule_found:
                new_state += "."
        initial_state = new_state

    a = int(-starting_point / 2)
    sum = 0
    for i in initial_state:
        if i == "#":
            sum += a
        a += 1
    print("The sum after 20 years: {}".format(sum))

    cur_answ = 0
    diff_set = set()
    # Got m from running manually and saw when the difference got constant.
    for m in range(0, 192):
        starting_point = 0
        initial_state = '###....#..#..#......####.#..##..#..###......##.##..#...#.##.###.##.###.....#.###..#.#.##.#..#.#'
        for gen in range(m):
            initial_state = "...." + initial_state + "...."
            starting_point += 4
            new_state = ""
            for i in range(len(initial_state)):
                current_state = initial_state[i:i + 5]
                rule_found = False
                for rule in rules:
                    if current_state in rule:
                        new_state += rule[current_state]
                        rule_found = True
                        break
                if not rule_found:
                    new_state += "."
            initial_state = new_state

        a = int(-starting_point / 2)
        sum = 0
        for i in initial_state:
            if i == "#":
                sum += a
            a += 1
        diff = sum - cur_answ
        cur_answ = sum

    # got 34 as a constant of change after 191 years
    result = (50000000000 - 191) * 34 + sum
    print("Result after 50000000000 years: {}".format(result))
