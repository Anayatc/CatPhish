import requests
from urllib.parse import urlparse
import whois
import re

url = 'http://amzn.to/2pfDiJE'
print(url)


# takes url as input and returns full url if url has been shortened.
def url_resolve(short_url):
    session = requests.Session()
    resp = session.head(short_url, allow_redirects=True)
    return resp.url


# takes the expanded url from url_resolve and returns just the domain name.
def domain_name():
    final_dest = url_resolve(url)
    parsed_uri = urlparse(final_dest)
    domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
    return domain


# returns the who.is information for the domain
def who_is():
    domain = domain_name()
    w = whois.whois(domain)
    print(w.text)
    print([i for i in w.text.split('\n')])
    return re.findall('Registrant', w.text)




print(url_resolve(url))
print(domain_name())
print(who_is())