#Time and Redirection in API Calls
#allow_redirects to get the first response code
#timout attribute to add wait

import requests

my_session = requests.session()
my_session.headers.update({'Content-Type': 'application/json'})
my_session.cookies.update({'visit-year': '2020', 'visit-month': 'December'})

res1 = my_session.get(
    url='https://httpbin.org/cookies',
    allow_redirects = False,
    timeout= 2
    )

print(res1.status_code)
print(res1.text)
print(res1.headers)