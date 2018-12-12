FILE_NAME = "input.txt"
INPUT = 3463

if __name__ == '__main__':
    # 300x300 grid
    result = [[0 for x in range(301)] for y in range(301)]
    for x in range(1, 301):
        for y in range(1, 301):
            rack_id = x + 10
            power_level = rack_id * y
            with_serial = power_level + INPUT
            mult = with_serial * rack_id
            r = ((mult // 100) % 10) - 5
            result[x][y] = r

    # Brute force
    maxx = 0
    for i in range(1, 301):
        for x in range(1, 301 - i):
            for y in range(1, 301 - i):

                res = 0
                for k in range(0, i):
                    for l in range(0, i):
                        res += result[k + x][l + y]
                if res > maxx:
                    maxx = res
                    # 233 282 11
                    print(x, y, i)
