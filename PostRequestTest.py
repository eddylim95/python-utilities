import requests

r = requests.post('http://127.0.0.1:5000/', json = {'data': 'test'})
print('Posted')
