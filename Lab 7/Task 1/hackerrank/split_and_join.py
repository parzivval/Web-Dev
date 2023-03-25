def split_and_join(line):
    a = "this is a string"
    a = a.split(" ")
    a = "-".join(a)
    return a
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)