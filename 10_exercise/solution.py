FILE_NAME = "input.txt"


def read_in_file(file_name):
    result = []
    with open(file_name, 'r') as input_file:
        for line in input_file:
            d = {}
            parts = line.strip("[\n").split("> ")
            d['x'] = int(parts[0].split(', ')[0].split('position=<')[1])
            d['y'] = int(parts[0].split(', ')[1])

            d['x_move'] = int(parts[1].split(', ')[0].strip('velocity=<'))
            d['y_move'] = int(parts[1].split(', ')[1].strip(">"))

            result.append(d)

    return result


def wait_a_second(i_list):
    for i in range(len(i_list)):
        i_list[i]['x'] += i_list[i]['x_move']
        i_list[i]['y'] += i_list[i]['y_move']


def get_min_max(i_list):
    mi_x = i_list[0]['x']
    ma_x = i_list[0]['x']
    mi_y = i_list[0]['y']
    ma_y = i_list[0]['y']
    for i in range(len(i_list)):
        if i_list[i]['x'] < mi_x:
            mi_x = i_list[i]['x']
        if i_list[i]['x'] > ma_x:
            mi_x = i_list[i]['x']
        if i_list[i]['y'] < mi_y:
            mi_y = i_list[i]['y']
        if i_list[i]['y'] > ma_y:
            ma_y = i_list[i]['y']

    return mi_x, ma_x, mi_y, ma_y


def print_message(minn_y, max_yy, minn_x, max_xx, i_list):
    for i in range(minn_y, max_yy + 1):
        mid_list = []
        for point in i_list:
            if point['y'] == i:
                mid_list.append(point)

        mid_list.sort(key=lambda x: x['x'])
        for j in range(minn_x - 30, max_xx + 30):
            found = False
            for el in mid_list:
                if el['x'] == j:
                    found = True
                    break
            if found:
                print("#", end="")
            else:
                print(".", end="")
        print()


if __name__ == '__main__':
    # {'x': 42532, 'y': -31649, 'x_move': -4, 'y_move': 3}
    input_list = read_in_file(FILE_NAME)

    seconds = 0
    while True:
        seconds += 1
        wait_a_second(input_list)
        min_x, max_x, min_y, max_y = get_min_max(input_list)
        # Manually found by getting the ones with diff < 100
        if max_y - min_y == 9:
            print("Y diff: {}".format(max_y - min_y))
            print("X diff: {}".format(max_x - min_x))
            break
    print("Seconds it took to get to it: {}".format(seconds))

    print_message(min_y, max_y, min_x, max_x, input_list)
