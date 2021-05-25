from sympy import nextprime, primerange

if __name__ == "__main__":
    list_count = [0, 0, 0, 0, [[2, 2]]]
    primes = list(primerange(1, 100))
    n = 5
    while len(list_count[-1]) <= 5000:
        temp = []
        if primes[-1] < n:
            primes.append(nextprime(n))
        for p1 in primes:
            if p1 >= n:
                break
            p2 = n - p1
            if n % p1 == 0:
                temp_2 = [p1 for i in range(int(n/p1))]
                temp.append(temp_2)
            else:
                if p2 > p1 and p2 in primes:
                    temp.append([p2, p1])
                if p2 > 3:
                    for k in list_count[p2]:
                        temp_3 = [p1]
                        for i in k:
                            temp_3.append(i)
                        temp_3.sort()
                        if temp_3 not in temp:
                            temp.append(temp_3)
        list_count.append(temp)
        n += 1
    print(f"Value: {n-1}, len: {len(list_count[-1])}")

