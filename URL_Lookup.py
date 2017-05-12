import requests
from urllib.parse import urlparse
import whois
from main import *

url = ''
print(url)


# add scheme to input url if not already there
def add_scheme(short_url):
    if url.startswith('http://') or url.startswith('https://'):
        return short_url
    if url.startswith('www.'):
        return 'http://' + short_url
    else:
        return 'http://' + short_url


# takes url as input and returns full url if url has been shortened.
def url_resolve():
    url_with_scheme = add_scheme(url)
    session = requests.Session()
    resp = session.head(url_with_scheme, allow_redirects=True)
    return resp.url


# takes the expanded url from url_resolve and returns just the domain name.
def domain_name():
    final_dest = url_resolve()
    parsed_uri = urlparse(final_dest)
    domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
    return domain


# returns the who.is information for the domain
def who_is():
    domain = domain_name()
    w = whois.whois(domain)
    print(w)
    return w.name, w.domain_name, w.registrar

print(add_scheme(url))
print(url_resolve())
print(domain_name())
print(who_is())