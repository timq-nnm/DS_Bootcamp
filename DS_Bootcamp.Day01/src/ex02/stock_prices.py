import sys

def stock_prices(arr):
    if len(arr) != 1:
        return
    
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
    
    if arr[0].capitalize() not in COMPANIES:
        print("Unknown company")
        return

    company = COMPANIES[arr[0].capitalize()]

    print(STOCKS[company])
    arr[0].to


if __name__ == '__main__':
    stock_prices(sys.argv[1:])