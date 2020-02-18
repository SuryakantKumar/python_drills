import re


def word_count(s):
    new = ''
    for x in s:
        if x >= 'a' and x <= 'z':
            new += x
        elif x >= 'A' and x <= 'Z':
            new += x
        elif x == ' ' or x == '-':
            new += x
        else:
            new += ''

    li = new.strip().split()

    count = {}
    for e in li:
        if e in count:
            count[e] += 1
        else:
            count[e] = 1

    return count


def dict_items(d):
    li = []
    for e in d:
        x = (e, d[e])
        li.append(x)

    return li


def dict_items_sorted(d):
    li = []
    for e in d:
        li.append(e)

    li = sorted(li)

    result = []
    for e in li:
        x = (e, d[e])
        result.append(x)

    return result


s = "Python is an interpreted, high-level, general-purpose programming language. Python interpreters are available for many operating systems. Python is a multi-paradigm programming language. Object-oriented programming and structured programming are fully supported."
word_count(s)
