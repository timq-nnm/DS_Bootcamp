import sys
import resource

def read_file_generator(filename):
        with open(filename, 'r') as file:
            for line in file:
                yield line

if __name__ == '__main__':
    start = resource.getrusage(resource.RUSAGE_SELF)

    if len(sys.argv) != 2:
        raise Exception('Invalid filename')
    
    filename = sys.argv[1]
    file_lines = read_file_generator(filename)

    for line in file_lines:
        pass

    stop = resource.getrusage(resource.RUSAGE_SELF)
    total_time = (stop.ru_utime + stop.ru_stime) - (start.ru_utime + start.ru_stime)
    memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / (1024 ** 3)
    print(f'{memory:.3f} GB')
    print(f'User Mode Time + System Mode Time = {total_time:.2f}s')


