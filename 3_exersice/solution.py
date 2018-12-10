FILE_NAME = "input.txt.txt"


def read_in_file(file_name):
    result = []
    with open(file_name, 'r') as input_file:
        for line in input_file:
            parts = line.split(" ")
            point_id = parts[0].strip("#")
            x_start = int(parts[2].split(",")[0])
            y_start = int(parts[2].split(",")[1].strip(":"))
            x_size = int(parts[3].split("x")[0])
            y_size = int(parts[3].split("x")[1].strip("\n"))
            result.append((x_start, y_start, x_size, y_size, point_id))

    return result


def find_overlaps(i_list):
    overlapping_points = set()
    points = set()
    for i in i_list:
        for j in range(i[0], i[0] + i[2]):
            for k in range(i[1], i[1] + i[3]):
                point = (j, k)
                if point in points:
                    overlapping_points.add(point)
                else:
                    points.add(point)

    return overlapping_points


def find_no_overlap(i_list, all_points):
    for i in i_list:
        overlap_found = False
        for j in range(i[0], i[0] + i[2]):
            for k in range(i[1], i[1] + i[3]):
                point = (j, k)
                if point in all_points:
                    overlap_found = True
                    break

            if overlap_found:
                break

        if overlap_found:
            continue
        else:
            return i


if __name__ == '__main__':
    # x_start, y_start, x_size, y_size
    input_list = read_in_file(FILE_NAME)
    o_points = find_overlaps(input_list)
    print("Overlapping points: {}".format(len(o_points)))

    no_overlap = find_no_overlap(input_list, o_points)
    print("ID with no overlap: {}".format(no_overlap[4]))
