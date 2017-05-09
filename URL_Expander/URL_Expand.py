import http.client
import urllib.parse
import urllib.request
import requests


def url_expand(url):
    parsed = urllib.parse.urlparse(url)
    h = http.client.HTTPConnection(parsed.netloc)
    h.request('HEAD', parsed.path)
    response = h.getresponse()
    if response.status/100 == 3 and response.getheader('Location'):
        return response.getheader('Location')
    else:
        return url + ' is direct path'


def url_resolve(url):
    session = requests.Session()
    resp = session.head(url, allow_redirects=True)
    return resp.url


print(url_resolve('http://amzn.to/2pfDiJE'))
print(url_resolve('https://goo.gl/Oha1fI'))
print(url_resolve('http://ow.ly/nFlK30byASt'))
