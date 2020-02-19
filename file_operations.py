def read_file(path):
    file = open(path, 'r')
    s = file.read()
    return s


def write_to_file(path, s):
    file = open(path, 'w')
    file.write(s)
    file.close()


def append_to_file(path, s):
    file = open(path, 'a')
    file.write(s)
    file.close()


def numbers_and_squares(n, file_path):
    file = open(file_path, 'w')
    for i in range(1, n+1):
        file.write(str(i)+',')
        file.write(str(i*i))
        if i < n:
            file.write('\n')
    file.close()
