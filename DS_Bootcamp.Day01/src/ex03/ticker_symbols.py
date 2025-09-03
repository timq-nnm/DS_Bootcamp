import sys

def ticker_symbols(arr):
    if len(arr) != 1: return
    
    COMPANIES = {
  'Apple': 'AAPL',
  'Microsoft': 'MSFT',
  'Netflix': 'NFLX',
  'Tesla': 'TSLA',
  'Nokia': 'NOK'
  }

    STOCKS = {
  'AAPL': 287.73,
  'MSFT': 173.79,
  'NFLX': 416.90,
  'TSLA': 724.88,
  'NOK': 3.37
  }
    ticker_up = arr[0].upper()
    
    if ticker_up not in STOCKS:
        print("Unknown company")
        return
    
    ticker = [key for key in COMPANIES if COMPANIES[key] == ticker_up]

    print(*ticker, STOCKS[ticker_up])



if __name__ == '__main__':
    ticker_symbols(sys.argv[1:])