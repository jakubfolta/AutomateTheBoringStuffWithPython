import webbrowser
#webbrowser.open('http://inventwithpython.com/')
import requests
import bs4

# res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
# print(type(res))
# res.status_code == requests.codes.ok
# print(len(res.text))
# print(res.text[:250])

# res = requests.get('http://inventwithpython.com/page_that_does_not_exists')
# try:
#     res.raise_for_status()
# except Exception as exc:
#     print('There was a problem: {}'.format(exc))

# res = requests.get('http://automatetheboringstuff.com/files/rj.txt')
# res.raise_for_status()
# play_file = open('RomeoAndJuliet.txt', 'wb')
# for chunk in res.iter_content(100000):
#     play_file.write(chunk)
#
# play_file.close()

res = requests.get('http://nostarch.com')
res.raise_for_status()
no_starch_soup = bs4.BeautifulSoup(res.text)
print(type(no_starch_soup))
