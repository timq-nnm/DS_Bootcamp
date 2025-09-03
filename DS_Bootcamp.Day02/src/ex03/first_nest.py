import sys

class Research:
    def __init__(self, argv):
        self.filepath = self.argv_checker(argv)


    @staticmethod
    def argv_checker(argv):
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


    def file_reader(self, has_header=True):
        file_data = self.file_checker()
        
        
        #valid_file?
        if has_header == True:
            if len(file_data) < 2 or \
                file_data[0] != 'head,tail' or \
                    file_data[1] not in ['0,1', '1,0']: raise Exception('Invalid file')
        else:
            if len(file_data) < 1 or \
                    file_data[1] not in ['0,1', '1,0']: raise Exception('Invalid file')

        file_data = [[int(number) for number in line.split(',')] for line in file_data[1:]]


        return file_data
    

    class Calculations:
        @staticmethod
        def count(data):
            result = [0, 0] # a - орел, b - решка

            for line in data:
                if line[0] == 1: result[0] += 1
                else: result[1] += 1

            
            return result


        def Fractions(orel, reshka):
            all_count = orel + reshka
            
            return orel / all_count * 100, reshka / all_count * 100
            
    

if __name__ == '__main__':
    research = Research(sys.argv)
    data = research.file_reader()

    orel, reshka  = Research.Calculations.count(data)
    fract_orel, fract_reshka = Research.Calculations.Fractions(orel, reshka)

    print(data) # список
    print(orel, reshka)
    print(fract_orel, fract_reshka)
