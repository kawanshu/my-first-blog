import requests
my_domain = 'kawanshu.pythonanywhere.com'
username = 'kawanshu'
token = 'e062fcdfc4c18568abb4a7098eb4fae87eefb3f2'

response = requests.post(
  'https://www.pythonanywhere.com/api/v0/user/{username}/webapps/{domain}/reload/'.format(
      username=username, domain=my_domain
  ),
  headers={'Authorization': 'Token {token}'.format(token=token)}
)
if response.status_code == 200:
  print('All OK')
else:
  print('Got unexpected status code {}: {!r}'.format(response.status_code, response.content))