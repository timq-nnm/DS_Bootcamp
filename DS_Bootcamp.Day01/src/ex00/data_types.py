def data_types():
    a = 1
    b = "Hello"
    c = 1.0
    d = True
    e = [1, 2, 3]
    f = (1, 2, 3)
    g = {1, 2, 3}
    h = {'a': 1}
    arr = [a, b, c, d, e, f, g, h]
    for i in arr:
        print(f'{i} : {type(i)}')

if __name__ == '__main__':
    data_types()
