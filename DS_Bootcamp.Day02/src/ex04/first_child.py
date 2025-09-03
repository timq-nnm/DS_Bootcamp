import sys
from random import randint

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
        def __init__(self, data):
            self.data = data
        

        def count(self):
            count_orel = sum(line[0] for line in self.data if line[0] == 1)
            count_reshka = sum(line[1] for line in self.data if line[1] == 1)
            
            return count_orel, count_reshka


        def Fractions(self):
            count_orel, count_reshka = self.count()
            all_count = count_orel + count_reshka
            
            return count_orel / all_count * 100, count_reshka / all_count * 100
        
    
    class Analytics(Calculations):
        @staticmethod
        def predict_random(number_predictions):
            result = []
            for count in range(number_predictions):
                orel = randint(0, 1)
    
                if orel == 0: reshka = 1
                else: reshka = 0
                result.append([orel, reshka])

            return result


        def predict_last(self):
            return self.data[-1]           
    

if __name__ == '__main__':
    research = Research(sys.argv)
    data = research.file_reader()
    data_calc = research.Calculations(data)
    data_analyt = research.Analytics(data)

    print(data) # список
    print(data_calc.count())
    print(data_calc.Fractions())
    print(data_analyt.predict_random(3))
    print(data_analyt.predict_last())