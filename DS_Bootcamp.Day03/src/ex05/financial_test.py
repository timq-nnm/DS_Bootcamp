import pytest
from financial import get_args, check_response, get_response

def test_get_args():
    ticker, metric = get_args(['financial.py', 'MSFT', 'Total Revenue'])
    assert  ticker == 'MSFT' and metric == 'Total Revenue'

def test_get_args_ticker():
    with pytest.raises(Exception):
        get_args(['financial.py', 'MSFFT', 'Total Revenue'])

def test_get_args_empty_args():
    with pytest.raises(Exception):
        get_args(['financial.py', 'MSFT'])