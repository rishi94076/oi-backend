import requests
from bs4 import BeautifulSoup

def fetch_oi_data(symbol='NIFTY'):
    url = f"https://www.nseindia.com/option-chain"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://www.nseindia.com"
    }
    with requests.Session() as session:
        session.headers.update(headers)
        response = session.get(url)
        cookies = session.cookies.get_dict()
        data_url = f"https://www.nseindia.com/api/option-chain-indices?symbol={symbol}"
        res = session.get(data_url, cookies=cookies)
        return res.json()
