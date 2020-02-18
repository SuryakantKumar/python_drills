def is_prime(n):
    d = 2
    while d < n:
        if n % d == 0:
            return False
        else:
            d += 1
    return True


def n_digit_primes(digit=2):
    li = []
    start = 10 ** (digit - 1)
    if start < 2:
        start = 2
    end = 10**(digit)

    while start < end:
        d = 2
        flag = True
        while d < start:
            if start % d == 0:
                flag = False
                break
            else:
                d += 1
        if flag == True:
            li.append(start)
        start += 1

    return li


print(n_digit_primes(1))
