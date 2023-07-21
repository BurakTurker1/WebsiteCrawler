import requests
from bs4 import BeautifulSoup
FoundLinks =[]
target_url_input = input("enter your target website: ")
target_url = "https://" + target_url_input


def request(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup


def crawler(url):
    links = request(url)
    for link in links.find_all('a'):
        found_link = link.get('href')
        if found_link:
            if '#' in found_link:
                found_link = found_link.split('#')[0]
            if target_url in found_link and found_link not in FoundLinks:
                FoundLinks.append(found_link)
                print(found_link)
                crawler(found_link)


crawler(target_url)
