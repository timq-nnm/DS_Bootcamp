import sys

class Research:
    def __init__(self, argv):
        self.filepath = self.argv_checker(argv)


    def argv_checker(self, argv):
        if argv[1:] == 0:
            raise Exception('Too much file argument')
        
        return argv[1]
    

    def file_checker(self):
        try:
            file_data = []
            with open(self.filepath, 'r') as file:
                for line in file:
                    line = line.strip()
                    if line:
                        file_data.append(line)
                        
            return file_data
        except FileNotFoundError:
            raise FileNotFoundError('File is not found')


    def file_reader(self):
        file_data = self.file_checker()
        
        #check_header
        if len(file_data) < 2 or \
              file_data[0] != 'head,tail' or \
                file_data[1] not in ['0,1', '1,0']: raise Exception('Invalid file')

        return '\n'.join(file_data)
    

if __name__ == '__main__':
    research = Research(sys.argv)
    print(research.file_reader())