import sys

def letter_starter(mail):
    f = open('employees.tsv', 'r')

    for line in f:
        name, surname, mail_in_list = line.split('\t')
        if mail[0] in mail_in_list:
            print(f'Dear {name}, welcome to our team. '
                  f'We are sure that it will be a pleasure to work with you. '
                  f'That’s a precondition for the professionals that our company hires.')
            break


if __name__ == '__main__':
    letter_starter(sys.argv[1:])