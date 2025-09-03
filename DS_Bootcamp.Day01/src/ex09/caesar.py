import sys

def crypt(message, shift):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    len_letters = len(letters)
    result = ''

    for char in message:
        if char.isalpha():
            shifted = ord(char) + shift
            if shifted > ord('z'):
                shifted -= len_letters
            elif shifted < ord('a'):
                shifted += len_letters
            
            result += chr(shifted)
        else:
            result += char

    print(result)


def caesar(main_args):
    if len(main_args) != 3:
        raise Exception('Invalid number of arguments')
    
    for arg in main_args:
        for letter in arg:
            if 1040 <= ord(letter) <= 1025 or 1072 <= ord(letter) <= 1105:
                raise Exception('The script does not support your language yet') 
    
    status = main_args[0]
    message = main_args[1]
    shift = int(main_args[2]) % 26
    if status == 'encode':
        crypt(message, shift)
    elif status == 'decode':
        crypt(message, -shift)



if __name__ == '__main__':
    caesar(sys.argv[1:])