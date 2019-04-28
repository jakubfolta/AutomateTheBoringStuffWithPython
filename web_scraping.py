import webbrowser
#webbrowser.open('http://inventwithpython.com/')
import requests

# res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
# print(type(res))
# res.status_code == requests.codes.ok
# print(len(res.text))
# print(res.text[:250])

res = requests.get('http://inventwithpython.com/page_that_does_not_exists')
res.raise_for_status()
