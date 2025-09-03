import timeit
import sys

def loop_append(arr):
    result_append = []

    for line in arr:
        if line.split('@')[1] == 'gmail.com':
            result_append.append(line)

    return result_append


def list_comprehension(arr):
    result_comprehension = [line for line in arr if line.split('@')[1] == 'gmail.com']

    return result_comprehension


def map_func(arr):
    return list(map(lambda arr: arr if arr.split('@')[1] == 'gmail.com' else None, arr))


def filter_func(arr):
    return list(filter(lambda arr: arr.split('@')[1] == 'gmail.com', arr))


def get_args(argv):
    if len(argv) != 3:
        raise Exception('Invalid arg count')
    
    return argv[1], int(argv[2])


def speedtest_func():
    benchmark_type, iteration = get_args(sys.argv)

    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com'] * 5
    
    if benchmark_type == 'loop':
        timed_run = timeit.timeit(lambda: loop_append(emails), number=iteration)
    elif benchmark_type == 'list_comprehension':
        timed_run = timeit.timeit(lambda: list_comprehension(emails), number=iteration)
    elif benchmark_type == 'map':
        timed_run = timeit.timeit(lambda: map_func(emails), number=iteration)
    elif benchmark_type == 'filter':
        timed_run = timeit.timeit(lambda: filter_func(emails), number=iteration)
    else:
        raise Exception('Invalid func type')
    
    print(f'{timed_run:.9f}')


if __name__ == '__main__':
    speedtest_func()