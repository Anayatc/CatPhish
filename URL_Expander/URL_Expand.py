import requests


def url_resolve(url):
    session = requests.Session()
    resp = session.head(url, allow_redirects=True)
    return resp.url

print(url_resolve('http://amzn.to/2pfDiJE'))
print(url_resolve('https://goo.gl/Oha1fI'))
print(url_resolve('http://ow.ly/nFlK30byASt'))
