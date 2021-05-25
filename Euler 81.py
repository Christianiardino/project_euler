if __name__ == "__main__":
    f = str(open("p081_matrix.txt", "r").read())
    m = []
    f = f.replace("\n", ",")
    f = f.split(",")

    for i in range(80):
        temp = []
        for j in range(80):
            temp.append(int(f[j + i*80]))
        m.append(temp)

    # m = [[131, 673, 234, 103, 18],
    #     [201, 96, 342, 965, 150],
    #     [630, 803, 746, 422, 111],
    #     [537, 699, 497, 121, 956],
    #     [805, 732, 524, 37, 331]]

    # m = [[13, 25, 12],
    #      [25, 12, 75],
    #      [12, 85, 11]]

    p = len(m[0])
    for c in range(p):
        for x in range(c + 1):
            y = c - x
            if x != 0 and y != 0:
                if m[x - 1][y] > m[x][y - 1]:
                    m[x][y] += m[x][y - 1]
                if m[x][y - 1] > m[x - 1][y]:
                    m[x][y] += m[x - 1][y]
                if m[x - 1][y] == m[x][y - 1]:
                    m[x][y] += m[x - 1][y]
                    print("Fudeu")
            else:
                if x == 0 and y != 0:
                    m[x][y] += m[x][y - 1]
                if x != 0 and y == 0:
                    m[x][y] += m[x - 1][y]

    for o in range(1, p):
        for x in range(o, p):
            y = p - x + (o - 1)
            if x != (p - 1) and y != (p - 1):
                if m[x - 1][y] > m[x][y - 1]:
                    m[x][y] += m[x][y - 1]
                if m[x][y - 1] > m[x - 1][y]:
                    m[x][y] += m[x - 1][y]
                if m[x - 1][y] == m[x][y - 1]:
                    m[x][y] += m[x - 1][y]
                    print("Fudeu")
            else:
                if x == (p - 1) and y != (p - 1):
                    m[x][y] += m[x - 1][y]
                if x != (p - 1) and y == (p - 1):
                    m[x][y] += m[x][y - 1]

    if m[-2][-1] > m[-1][-2]:
        m[-1][-1] += m[-1][-2]
    else:
        m[-1][-1] += m[-2][-1]

    print(m[-1][-1])