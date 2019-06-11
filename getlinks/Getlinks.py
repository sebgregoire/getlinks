import requests
from html.parser import HTMLParser

class Getlinks:
    def __init__(self, url):
        self.url = url
        self.parser = LinksParser()
        self.request = requests.request('GET', url)
        self.parser.feed(self.request.text)

    def listLinks(self, unique=False):
        if unique:
            links = list()
            for link in self.parser.links:
                if link not in links:
                    links.append(link)

            return links
        else:
            return self.parser.links


class LinksParser(HTMLParser):
    links = list()

    def handle_starttag(self, tag, attrs):
        if 'a' in tag:
            for attr in attrs:
                if 'href' in attr:
                    _, link = attr
                    self.links.append(link)

