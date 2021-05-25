from itertools import permutations

pins = [319, 680, 180, 690, 129, 620, 762, 689, 762, 318, 368, 710, 720, 710, 629, 168, 160, 689, 716, 731,
        736, 729, 316, 729, 729, 710, 769, 290, 719, 680, 318, 389, 162, 289, 162, 718, 729, 319, 790, 680,
        890, 362, 319, 760, 316, 729, 380, 319, 728, 716]

if __name__ == "__main__":
    count_1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    count_2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    count_3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    numbers_used = [False for i in range(10)]

    for p in pins:
        numbers_used[int(str(p)[0])] = True
        numbers_used[int(str(p)[1])] = True
        numbers_used[int(str(p)[2])] = True
        count_1[int(str(p)[0])] += 1
        count_2[int(str(p)[1])] += 1
        count_3[int(str(p)[2])] += 1

    perm_list = []
    for n in range(len(numbers_used)):
        if numbers_used[n]:
            perm_list.append(n)

    perm_list = list(permutations(perm_list))

    for i in range(10):
        print(f"i = {i}, count_1[i]: {count_1[i]}")
    print("\n\n")
    for i in range(10):
        print(f"i = {i}, count_2[i]: {count_2[i]}")
    print("\n\n")
    for i in range(10):
        print(f"i = {i}, count_3[i]: {count_3[i]}")
    print("\n\n")