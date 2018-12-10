import time

FILE_NAME = "input.txt"


def read_in_file(file_name):
    with open(file_name, 'r') as input_file:
        for line in input_file:
            return line.strip()


def chemical_reaction(i_str):
    buffer = []
    for char in i_str:

        if buffer and char != buffer[-1] and char.lower() == buffer[-1].lower():
            buffer.pop()
        else:
            buffer.append(char)

    return buffer


if __name__ == '__main__':
    s = time.time()
    chem = read_in_file(FILE_NAME)
    new_chem = chemical_reaction(chem)

    print("Units in final chem: {}".format(len(new_chem)))
    print("Part 1 time: {}s".format(round(time.time() - s, 2)))

    s = time.time()
    chars = {i.lower() for i in chem}
    min_chem = None
    for c in chars:
        reduced_chem = ([char for char in chem if char.lower() != c])
        r_chem_len = len(chemical_reaction(reduced_chem))
        if not min_chem:
            min_chem = r_chem_len
            continue
        if r_chem_len < min_chem:
            min_chem = r_chem_len

    print("Lowest chem: {}".format(min_chem))
    print("Part 2 time: {}s".format(round(time.time() - s, 2)))
