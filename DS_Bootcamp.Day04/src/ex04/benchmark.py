import timeit
import random
from collections import Counter

def generate_values():
    numbers = [random.randint(0, 100) for i in range(1000000)]

    return numbers


def my_func_count(numbers):
    counts = {i: 0 for i in range(101)}

    for num in numbers:
        counts[num] += 1

    return counts


def top_10_numbers(numbers):
    counts = my_func_count(numbers)

    top_10_list = sorted(counts.items(), key=lambda item: item[1],reverse=True)

    return dict(top_10_list[:10])


def counter_func_count(numbers):
    return Counter(numbers)


def top_10_counter_func(numbers):
    return dict(Counter(numbers).most_common(10))


def speedtest_func():
    numbers = generate_values()
    iteration = 100

    my_func_time = timeit.timeit(lambda: my_func_count(numbers), number=iteration)
    counter_func_time = timeit.timeit(lambda: counter_func_count(numbers), number=iteration)

    my_top_10_time = timeit.timeit(lambda: top_10_counter_func(numbers), number=iteration) 
    counter_top_10_time = timeit.timeit(lambda: top_10_counter_func(numbers), number=iteration)

    print(f"my function: {my_func_time}")
    print(f"Counter: {counter_func_time}")
    print(f"my top: {my_top_10_time}")
    print(f"Counter`s time: {counter_top_10_time}")


if __name__ == '__main__':
    speedtest_func()