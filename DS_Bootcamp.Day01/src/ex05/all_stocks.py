import sys

def all_stocks(arr):
    if (len(arr) != 1): return

    normalize_companies = [x.strip() for x in arr[0].split(',')]

    if '' in normalize_companies: return

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
    
    for company in normalize_companies:
        company_upper = company.upper()
        company_capitalize = company.capitalize()

        if company_upper in STOCKS:
            company_values = list(COMPANIES.values())
            company_values_index = company_values.index(company_upper)
            company_keys = list(COMPANIES.keys())

            print(f"{company_upper} is a ticker symbol for {company_keys[company_values_index]}")
        elif company_capitalize in COMPANIES:
            ticker = COMPANIES[company_capitalize]
            print(f"{company_capitalize} stock price is {STOCKS[ticker]}")
        else:
            print(f"{company} is an unknown company or an unknown ticker symbol")

if __name__ == '__main__':
    all_stocks(sys.argv[1:])