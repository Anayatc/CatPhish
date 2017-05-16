import requests
from urllib.parse import urlparse
import whois


# takes url as input and returns full url if url has been shortened.
def url_resolve(url):

    if url.startswith('http://') or url.startswith('https://'):
        session = requests.Session()
        resp = session.head(url, allow_redirects=True)
        global url_with_scheme
        url_with_scheme = resp.url
        return url_with_scheme
    if url.startswith('www.'):
        url = 'http://' + url
        session = requests.Session()
        resp = session.head(url, allow_redirects=True)
        url_with_scheme = resp.url
        return url_with_scheme
    else:
        url = 'http://' + url
        session = requests.Session()
        resp = session.head(url, allow_redirects=True)
        url_with_scheme = resp.url
        return url_with_scheme


# takes the expanded url from url_resolve and returns just the domain name.
def domain_name():
    final_dest = url_resolve(url_with_scheme)
    parsed_uri = urlparse(final_dest)
    domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
    return domain


# returns the who.is information for the domain
def who_is():
    domain = domain_name()
    w = whois.whois(domain)
    print(w.text)
    return w.name, w.domain_name, w.registrar, w.text
