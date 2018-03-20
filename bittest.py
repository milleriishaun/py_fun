# use requests to get data in json form
import requests

r = requests.get('https://api.coindesk.com/v1/bpi/historical/close.json?start=2016-03-19&end=2018-03-19', verify=False)

# real data from past month
# get the BitCoin Price Index
for k, v in r.json()['bpi'].items():
    print(k, v)

