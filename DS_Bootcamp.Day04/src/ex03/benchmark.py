import timeit
import sys
from functools import reduce

def get_args(argv):
    if len(argv) != 4:
        raise Exception('Invalid arg count')
    
    return argv[1], int(argv[2]), int(argv[3])


def sum_square(number):
    sum = 0
    for x in range(1, number + 1):
        sum = sum + x * x

    return sum


def sum_square_reduce(x, y):
    return x + y * y


def reduce_func(number):
    return reduce(sum_square_reduce, range(1, number + 1))


def speedtest_func():
    benchmark_type, iteration, numbers = get_args(sys.argv)

    func = {
        'loop' : lambda: sum_square(numbers),
        'reduce' : lambda: reduce_func(numbers)
    }

    try:
        timed_run = timeit.timeit(func[benchmark_type], number=iteration)
    except:
        raise Exception('Invalid operation')

    print(f'{timed_run:.9f}')


if __name__ == '__main__':
    speedtest_func()