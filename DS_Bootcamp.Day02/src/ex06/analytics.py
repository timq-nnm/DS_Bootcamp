import sys
from random import randint
import logging
import requests
from config import BOT_TOKEN, CHAT_ID, TELEGRAM_URL 

class Research:
    def __init__(self, argv):
        self.filepath = self.argv_checker(argv)
        logging.info(f'Initialization of Research class with file: {self.filepath}')

    @staticmethod
    def send_to_telegram(message):
        logging.info('Sending a message to Telegram')

        params = {
            'chat_id': CHAT_ID,
            'text': message
        }

        try:
            response = requests.get(TELEGRAM_URL, params=params)

            if response.status_code == 200:
                logging.info(f'The message was successfully sent to Telegram. Response status: {response.status_code}')
        except Exception:
                logging.info(f'The message was not sent to Telegram. Response status: {response.status_code}')
                raise Exception(f'The message was not sent to Telegram. Response status: {response.status_code}')


    @staticmethod
    def argv_checker(argv):
        if argv[1:] == 0:
            logging.warning(f'Invalid file argument: {argv}')
            raise Exception('Invalid file argument')
        
        return argv[1]


    def file_checker(self):
        try:
            file_data = []
            with open(self.filepath, 'r') as file:
                for line in file:
                    line = line.strip()
                    if line:
                        file_data.append(line)

            logging.info(f'The file has been successfully read: {self.filepath}')

            return file_data
        except FileNotFoundError:
            logging.warning(f'Invalid file: {self.filepath}')
            raise FileNotFoundError('Invalid file')


    def file_reader(self, has_header=True):
        file_data = self.file_checker()
        
        
        #valid_file?
        if has_header == True:
            if len(file_data) < 2 or \
                file_data[0] != 'head,tail' or \
                    file_data[1] not in ['0,1', '1,0']: 
                    logging.warning(f'Invalid file content')
                    raise Exception('Invalid file content')
        else:
            if len(file_data) < 1 or \
                    file_data[1] not in ['0,1', '1,0']:
                    logging.warning(f'Invalid file content')
                    raise Exception('Invalid file content')

        file_data = [[int(number) for number in line.split(',')] for line in file_data[1:]]

        logging.info('The contents of the file are correct')

        return file_data
    

    class Calculations:
        def __init__(self, data):
            self.data = data
            logging.info('Initializing Calculations(Subclass Research)')
        

        def count(self):
            count_orel = sum(line[0] for line in self.data if line[0] == 1)
            count_reshka = sum(line[1] for line in self.data if line[1] == 1)
            
            logging.info('The number of heads and tails has been successfully counted')

            return count_orel, count_reshka


        def Fractions(self):
            count_orel, count_reshka = self.count()
            all_count = count_orel + count_reshka
            
            logging.info('Successfully calculated the percentage of heads and tails')

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

            logging.info('Successfully generated a random list of eagle and tails')

            return result
        
        @staticmethod
        def predict_random_count(prediction):
            forecast_total = len(prediction)
            forecast_heads = sum(head[0] for head in prediction)
            forecast_tails = sum(tail[1] for tail in prediction)

            logging.info('A random list of eagle and tails has been successfully tallied')

            return forecast_total, forecast_heads, forecast_tails


        def predict_last(self):
            logging.info('The last element of the random list was successfully transferred')

            return self.data[-1]
        

        @staticmethod
        def save_file(result, filename, file_extension):
            try:
                with open(f'{filename}.{file_extension}', 'w') as file:
                    file.write(result)
                logging.info(f'The file was successfully saved: {filename}.{file_extension}')
            except Exception:
                logging.warning(f'The report has not been saved: {filename}.{file_extension}')
                raise Exception(f'The report has not been saved: {filename}.{file_extension}')