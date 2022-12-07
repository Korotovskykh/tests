import requests

print('Test check status code')
r = requests.get('https://github.com')
assert r.status_code == 200
print('Status code is 200 OK')
