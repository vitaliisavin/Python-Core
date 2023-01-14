import json
import requests

available_currency = str.lower(input())
desired_currency = ''
available_sum = 0
currency_rates = {}

r = requests.get(f'https://www.floatrates.com/daily/{available_currency}.json')
dict_r = json.loads(r.text)
if available_currency != 'usd':
    currency_rates['usd'] = dict_r['usd']['rate']
if available_currency != 'eur':
    currency_rates['eur'] = dict_r['eur']['rate']

while True:
    desired_currency = str.lower(input())
    if desired_currency == '':
        break
    available_sum = int(input())
    print('Checking the cache...')
    if desired_currency in currency_rates:
        print('Oh! It is in the cache!')
        result = round(available_sum * currency_rates[desired_currency], 2)
        print(f'You received {result} {str.upper(desired_currency)}.')
    else:
        print('Sorry, but it is not in the cache!')
        currency_rates[desired_currency] = dict_r[desired_currency]['rate']
        result = round(available_sum * currency_rates[desired_currency], 2)
        print(f'You received {result} {str.upper(desired_currency)}.')



