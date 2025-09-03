import sys

def names_extractor(path):
    f = open(path[0])
    mails_list = [_ for _ in f.read().split('\n')]

    names_list = list()

    for mail in range(len(mails_list)):
        name = mails_list[mail].split('.')[0]
        surname = mails_list[mail].split('.')[1].split('@')[0]

        names_list.append([name, surname, mails_list[mail]])


    output = open('employees.tsv', 'w')

    output.write(f'Name\tSurname\tE-mail\n')

    for employee in names_list:
        output.write(f'{employee[0].capitalize()}\t{employee[1].capitalize()}\t{employee[2]}\n')

if __name__ == '__main__':
    names_extractor(sys.argv[1:])