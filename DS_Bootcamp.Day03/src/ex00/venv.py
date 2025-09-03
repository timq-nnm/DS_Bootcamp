import os
def print_env():
    print('Your current virtual env is: ',os.getenv('VIRTUAL_ENV'))

if __name__ == '__main__':
    print_env()