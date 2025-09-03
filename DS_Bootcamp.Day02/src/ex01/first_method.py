class Research:
    def file_reader(self):
        f = open('data.csv', 'r')
        return f.read()


if __name__ == '__main__':
    print(Research().file_reader())