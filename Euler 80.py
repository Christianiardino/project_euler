from decimal import *
from math import ceil

getcontext().prec = 110

if __name__ == "__main__":
    numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    count = 0
    for n in range(2, 100):
        if n not in numbers:
            a = ceil(int(pow(n, 1/2))/10)
            print(a, n)
            temp = str(int((Decimal.sqrt(Decimal(n)))*pow(10, 100)))[0:100]
            for c in temp:
                count += int(c)
    print(count)