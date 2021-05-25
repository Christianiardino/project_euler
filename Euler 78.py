def pent_calc(n):
    return int((3*n*n - n)/2)


if __name__ == "__main__":
    pent = []
    for p in range(1, 1000):
        pent.append(pent_calc(p))
        pent.append(pent_calc(-p))
    part = [1, 1, 2]
    n = 3
    while True:
        part.append(0)
        count = 0
        pos = True
        for p in pent:
            if n - p >= 0:
                if pos:
                    part[n] += part[n - p]
                else:
                    part[n] -= part[n - p]
                #print(f"n : {n}, flip, {pos}, n - p: {n - p}, part[p] = {part[n - p]}")
                count += 1
                if count == 2:
                    count = 0
                    if pos:
                        pos = False
                    else:
                        pos = True
            else:
                break
        part[n] %= 1000000
        if part[n] % 1000000 == 0:
            print(f"Result : {n}")
            break
        n += 1