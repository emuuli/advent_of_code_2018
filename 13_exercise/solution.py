FILE_NAME = "input.txt"
CARTS = "^v<>"
CROSS_ORDER = ["left", "straight", "right"]
CROSS = "+"


class Cart:
    def __init__(self, x, y, type, last_type):
        self.x = x
        self.y = y
        self.type = type
        self.last_x = 0
        self.last_y = 0
        self.last_type = last_type
        self.last_cross = "right"
        self.dead = False

    def get_next_cross(self):
        next_index = CROSS_ORDER.index(self.last_cross) + 1
        if next_index >= len(CROSS_ORDER):
            next_index = 0

        if next_index == 0:
            if self.type == "^":
                dir = "<"
            if self.type == "v":
                dir = ">"
            if self.type == "<":
                dir = "v"
            if self.type == ">":
                dir = "^"
        elif next_index == 2:
            if self.type == "^":
                dir = ">"
            if self.type == "v":
                dir = "<"
            if self.type == "<":
                dir = "^"
            if self.type == ">":
                dir = "v"
        else:
            dir = self.type

        return CROSS_ORDER[next_index], dir

    def move(self, grid):
        if self.type == "^":
            next_stop = grid[self.x - 1][self.y]
            if next_stop in CARTS:
                return self.x - 1, self.y

            if next_stop == CROSS:
                grid[self.x][self.y] = self.last_type
                self.last_type = CROSS
                self.last_cross, self.type = self.get_next_cross()
                self.x -= 1
                grid[self.x][self.y] = self.type

            if next_stop == "/":
                grid[self.x][self.y] = self.last_type
                self.last_type = next_stop
                self.x -= 1
                self.type = ">"
                grid[self.x][self.y] = self.type

            if next_stop == "\\":
                grid[self.x][self.y] = self.last_type
                self.last_type = next_stop
                self.x -= 1
                self.type = "<"
                grid[self.x][self.y] = self.type

            if next_stop == "|":
                grid[self.x][self.y] = self.last_type
                self.last_type = next_stop
                self.x -= 1
                grid[self.x][self.y] = self.type

        elif self.type == "v":
            next_stop = grid[self.x + 1][self.y]
            if next_stop in CARTS:
                return self.x + 1, self.y

            if next_stop == CROSS:
                grid[self.x][self.y] = self.last_type
                self.last_type = CROSS
                self.last_cross, self.type = self.get_next_cross()
                self.x += 1
                grid[self.x][self.y] = self.type

            if next_stop == "/":
                grid[self.x][self.y] = self.last_type
                self.last_type = next_stop
                self.x += 1
                self.type = "<"
                grid[self.x][self.y] = self.type

            if next_stop == "\\":
                grid[self.x][self.y] = self.last_type
                self.last_type = next_stop
                self.x += 1
                self.type = ">"
                grid[self.x][self.y] = self.type

            if next_stop == "|":
                grid[self.x][self.y] = self.last_type
                self.last_type = next_stop
                self.x += 1
                grid[self.x][self.y] = self.type

        elif self.type == "<":
            next_stop = grid[self.x][self.y - 1]
            if next_stop in CARTS:
                return self.x, self.y - 1

            if next_stop == CROSS:
                grid[self.x][self.y] = self.last_type
                self.last_type = CROSS
                self.last_cross, self.type = self.get_next_cross()
                self.y -= 1
                grid[self.x][self.y] = self.type

            if next_stop == "/":
                grid[self.x][self.y] = self.last_type
                self.last_type = next_stop
                self.y -= 1
                self.type = "v"
                grid[self.x][self.y] = self.type

            if next_stop == "\\":
                grid[self.x][self.y] = self.last_type
                self.last_type = next_stop
                self.y -= 1
                self.type = "^"
                grid[self.x][self.y] = self.type

            if next_stop == "-":
                grid[self.x][self.y] = self.last_type
                self.last_type = next_stop
                self.y -= 1
                grid[self.x][self.y] = self.type

        elif self.type == ">":
            next_stop = grid[self.x][self.y + 1]
            if next_stop in CARTS:
                return self.x, self.y + 1

            if next_stop == CROSS:
                grid[self.x][self.y] = self.last_type
                self.last_type = CROSS
                self.last_cross, self.type = self.get_next_cross()
                self.y += 1
                grid[self.x][self.y] = self.type

            if next_stop == "/":
                grid[self.x][self.y] = self.last_type
                self.last_type = next_stop
                self.y += 1
                self.type = "^"
                grid[self.x][self.y] = self.type

            if next_stop == "\\":
                grid[self.x][self.y] = self.last_type
                self.last_type = next_stop
                self.y += 1
                self.type = "v"
                grid[self.x][self.y] = self.type

            if next_stop == "-":
                grid[self.x][self.y] = self.last_type
                self.last_type = next_stop
                self.y += 1
                grid[self.x][self.y] = self.type


def read_in_file(file_name):
    result = []
    number_of_lines = 0
    longest_line = 0
    with open(file_name, 'r') as input_file:
        for line in input_file:
            line = line.strip("\n")
            longest_line = len(line) if len(line) > longest_line else longest_line
            number_of_lines += 1
            result.append(line)

    return result, longest_line, number_of_lines


def fill_empty_spots(i_list, x_len, y_len):
    result = [["" for x in range(y_len)] for y in range(x_len)]
    for i in range(x_len):
        for j in range(y_len):
            if j >= len(i_list[i]):
                result[i][j] = ""
            else:
                result[i][j] = i_list[i][j]
    return result


def is_cart(point):
    return point in CARTS and point != ""


def map_carts(x, y, grid):
    list_of_carts = []
    for i in range(x):
        for j in range(y):
            point = grid[i][j]
            if is_cart(point):
                if point in "<>":
                    last_type = "-"
                else:
                    last_type = "|"
                list_of_carts.append(Cart(i, j, point, last_type))
    return list_of_carts


def list_carts(list_of_carts):
    s = sorted(list_of_carts, key=lambda x: (x.x, x.y))
    return s


if __name__ == '__main__':
    input_file, y, x = read_in_file(FILE_NAME)
    input_file = fill_empty_spots(input_file, x, y)
    list_of_carts = map_carts(x, y, input_file)
    list_of_active_carts = len(list_of_carts)
    while list_of_active_carts > 2:
        for cart in list_of_carts:
            if not cart.dead:
                crash = cart.move(input_file)
                if crash:
                    print(crash[1], crash[0])
                    cart.dead = True
                    for c_cart in list_of_carts:
                        if c_cart.x == crash[0] and c_cart.y == crash[1]:
                            c_cart.dead = True
                            break

        list_of_active_carts = 0
        list_of_carts = list_carts(list_of_carts)
        for c in list_of_carts:
            if not c.dead:
                list_of_active_carts += 1
