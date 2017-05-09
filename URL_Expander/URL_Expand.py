import http.client
import urllib.parse


def url_expand(url):
    parsed = urllib.parse.urlparse(url)
    h = http.client.HTTPConnection(parsed.netloc)
    h.request('HEAD', parsed.path)
    response = h.getresponse()
    if response.status/100 == 3 and response.getheader('Location'):
        return response.getheader('Location')
    else:
        return url + ' is direct path'


print(url_expand('http://amzn.to/2pfDiJE'))
print(url_expand('https://goo.gl/Oha1fI'))
