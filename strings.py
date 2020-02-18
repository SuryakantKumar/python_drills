def last_3_characters(x):
    if len(x) <= 3:
        return x
    return x[len(x)-3:]


def first_10_characters(x):
    if len(x) <= 10:
        return x
    return x[0:10]


def chars_4_through_10(x):
    if len(x) <= 5:
        return ""
    return x[4:11]


def str_length(x):
    return len(x)


def words(x):
    return x.strip().split()


def capitalize(x):
    return x.capitalize()


def to_uppercase(x):
    return x.upper()
