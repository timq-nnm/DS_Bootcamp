import timeit

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
    return map(lambda arr: arr if arr.split('@')[1] == 'gmail.com' else None, arr)


def speedtest_func():
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com'] * 5

    iteration = 90_000_000 #90000000

    timed_run1 = timeit.timeit(lambda: loop_append(emails), number=iteration)
    timed_run2 = timeit.timeit(lambda: list_comprehension(emails), number=iteration)
    timed_run3 = timeit.timeit(lambda: map_func(emails), number=iteration)

    times = {
        'loop_append' : timed_run1,
        'list_comprehension' : timed_run2,
        'map_func' : timed_run3
    }

    min_time = min(times, key=times.get)
    print(f'it is better to use a {min_time}')

    result_times = sorted(times.items(), key=lambda x: x[1])
    
    print(f'{result_times[0][1]} vs {result_times[1][1]} vs {result_times[2][1]}')


if __name__ == '__main__':
    speedtest_func()
