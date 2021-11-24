from bs4 import BeautifulSoup
import requests
url = "https://google.com.ua"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
dictionary = {}

for link in soup.find_all('a'):
    url=link.get('href')
    title=soup.title.text
    if 'http' in str(url):
        dictionary[title]=url
        print(dictionary)
        

