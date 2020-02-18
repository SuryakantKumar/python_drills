def sum_items_in_list(x):
    sum = 0
    for e in x:
        sum += e
    return sum


def list_length(x):
    return len(x)


def last_three_items(x):
    if len(x) <= 3:
        return x
    return x[len(x)-3:]


def first_three_items(x):
    if len(x) <= 3:
        return x
    return x[:3]


def sort_list(x):
    return sorted(x)


def append_item(x, item):
    x.append(item)
    return x


def remove_last_item(x):
    return x[:len(x)-1]


def count_occurrences(x, item):
    count = 0
    for e in x:
        if e == item:
            count += 1
    return count


def is_item_present_in_list(x, item):
    return item in x


def append_all_items_of_y_to_x(x, y):
    x.extend(y)
    return x


def list_copy(x):
    return x.copy()
