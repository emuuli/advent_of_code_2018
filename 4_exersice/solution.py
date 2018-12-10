FILE_NAME = "input.txt"


def read_in_file(file_name):
    result = []
    with open(file_name, 'r') as input_file:
        for line in input_file:
            d = {}
            parts = line.strip("[\n").split("] ")
            d['ts'] = parts[0]
            d['msg'] = parts[1]
            result.append(d)

    result.sort(key=lambda x: x['ts'])

    return result


def get_guard_sleep(i_list):
    guards = {}
    guard = ""
    for i in range(len(i_list)):
        if "Guard" in i_list[i]['msg']:
            guard = i_list[i]['msg'].split("#")[1].split(" ")[0]
            if guard not in guards:
                guards[guard] = {}
        if "falls" in i_list[i]['msg']:
            wake_up_min = int(i_list[i + 1]['ts'].split(":")[1]) - 1
            fall_sleep_min = int(i_list[i]['ts'].split(":")[1])
            minutes_slept = wake_up_min - fall_sleep_min

            if 'minutes_slept' not in guards[guard]:
                guards[guard]['minutes_slept'] = minutes_slept
                guards[guard]['minute_count'] = {}
            else:
                guards[guard]['minutes_slept'] += minutes_slept

            for j in range(fall_sleep_min, wake_up_min):
                if str(j) not in guards[guard]['minute_count']:
                    guards[guard]['minute_count'][str(j)] = 0
                guards[guard]['minute_count'][str(j)] += 1

    # print(guards)
    return guards


def get_biggest_sleeper(guard_dict):
    b_sleeper = {}
    for key, value in guard_dict.items():
        if 'minutes_slept' not in value or 'minute_count' not in value:
            continue
        if not b_sleeper:
            b_sleeper["id"] = key
            b_sleeper["value"] = value
            continue

        if value['minutes_slept'] > b_sleeper['value']['minutes_slept']:
            b_sleeper['id'] = key
            b_sleeper['value'] = value

    # print(biggest_sleeper)

    minutes_dict = b_sleeper['value']['minute_count']
    # print(minutes_dict)
    minute_list = []
    for key, value in minutes_dict.items():
        r = {'key': key, 'value': value}
        minute_list.append(r)
    minute_list.sort(key=lambda x: x['value'])
    # print(minute_list)
    b_sleeper['biggest_minute'] = minute_list[-1]['key']
    return b_sleeper


def get_biggest_sleeper_2(guard_dict):
    b_sleeper = {}
    for key, value in guard_dict.items():
        if 'minutes_slept' not in value or 'minute_count' not in value:
            continue
        if not b_sleeper:
            b_sleeper["id"] = key
            b_sleeper["value"] = value

            minutes_dict = value['minute_count']
            minute_list = []
            for key_2, value_2 in minutes_dict.items():
                r = {'key': key_2, 'value': value_2}
                minute_list.append(r)
            minute_list.sort(key=lambda x: x['value'])
            b_sleeper['biggest_minute_key'] = minute_list[-1]['key']
            b_sleeper['biggest_minute'] = minute_list[-1]['value']
            continue

        else:
            minutes_dict = value['minute_count']
            minute_list = []
            for key_2, value_2 in minutes_dict.items():
                r = {'key': key_2, 'value': value_2}
                minute_list.append(r)
            minute_list.sort(key=lambda x: x['value'])

            if minute_list[-1]['value'] > b_sleeper['biggest_minute']:
                b_sleeper["id"] = key
                b_sleeper["value"] = value
                b_sleeper['biggest_minute_key'] = minute_list[-1]['key']
                b_sleeper['biggest_minute'] = minute_list[-1]['value']

    return b_sleeper


if __name__ == '__main__':
    input_list = read_in_file(FILE_NAME)
    # for l in input_list:
    # print(l)
    guard_sleep = get_guard_sleep(input_list)
    # for key, value in guard_sleep.items():
    #     print(key, value)
    biggest_sleeper = get_biggest_sleeper(guard_sleep)
    # print(biggest_sleeper)
    print("Biggest sleeper ID: {}".format(biggest_sleeper['id']))
    print("Biggest sleeper biggest minute: {}".format(biggest_sleeper['biggest_minute']))
    print("Answer: {}".format(int(biggest_sleeper['id']) * int(biggest_sleeper['biggest_minute'])))

    print("")
    biggest_sleeper_2 = get_biggest_sleeper_2(guard_sleep)
    print("Biggest sleeper ID: {}".format(biggest_sleeper_2['id']))
    print("Biggest sleeper biggest minute: {}: {}".format(biggest_sleeper_2['biggest_minute_key'],
                                                          biggest_sleeper_2['biggest_minute']))
    print("Answer: {}".format(int(biggest_sleeper_2['id']) * int(biggest_sleeper_2['biggest_minute_key'])))
