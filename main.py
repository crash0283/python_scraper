import requests
import bs4
import urllib.request


def getUrl(url: str):
    myUrl = requests.get(url)
    return myUrl.text


htmlparser = getUrl('https://unsplash.com/s/photos/flowers')

if htmlparser is not None:
    soup = bs4.BeautifulSoup(htmlparser, 'html.parser')

    for i, image in enumerate(soup.find_all('img')):
        urllib.request.urlretrieve(image['src'], f'C:/Users/rasch/Desktop/scraper/pic{i}.jpg')
        print(f'pic{i} downloaded!')
else:
    print("File Not Available!")
