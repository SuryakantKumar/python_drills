def add3(a, b, c):
    return sum([a, b, c])


def unpacking1():
    items = [1, 2, 3]
    return add3(*items)


def unpacking2():
    kwargs = {'a': 1, 'b': 2, 'c': 3}
    return add3(**kwargs)


def call_function_using_keyword_arguments_example():
    a = 1
    b = 2
    c = 3
    return add3(a, b, c)


def add_n(*n):
    sum = 0
    for e in n:
        sum += e
    return sum


def add_kwargs(a, b):
    return a + b


def universal_acceptor(*args, **kwargs):
    if args and kwargs:
        print(args, kwargs)
    elif args:
        print(args)
    else:
        print(kwargs)
