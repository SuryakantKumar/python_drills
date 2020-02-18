def integers_from_start_to_end_using_range(start, end, step):
    li = []
    for i in range(start, end, step):
        li.append(i)
    return li


def integers_from_start_to_end_using_while(start, end, step):
    if step >= 0:
        li = []
        while start < end:
            li.append(start)
            start += step
        return li
    else:
        li = []
        while start > end:
            li.append(start)
            start += step
        return li


def two_digit_primes():
    li = []
    start = 11
    end = 97

    while start <= end:
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


print(two_digit_primes())
