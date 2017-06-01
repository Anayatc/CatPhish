from URL_Lookup import *


def test_add_scheme():
    assert(url_resolve('ow.ly/i5AX30bCN5s') == 'http://ow.ly/i5AX30bCN5s')
    assert(url_resolve('google.com') == 'http://google.com')
    assert(url_resolve('www.google.com') == 'http://www.google.com')
    assert(url_resolve('www.amazon.com') == 'http://www.amazon.com')
    assert(url_resolve('www.ebay.com') == 'http://www.ebay.com')
    assert(url_resolve('www.paypal.com') == 'http://www.paypal.com')
    assert(url_resolve('www.reddit.com') == 'http://www.reddit.com')
    assert(url_resolve('www.apple.com') == 'http://www.apple.com')
    assert(url_resolve('www.github.com') == 'http://www.github.com')
    assert(url_resolve('www.quora.com') == 'http://www.quora.com')
    assert(url_resolve('www.lloydsbank.com') == 'http://www.lloydsbank.com')
    assert(url_resolve('www.hsbc.com') == 'http://www.hsbc.com')
    assert(url_resolve('www.barclays.com') == 'http://www.barclays.com')
    assert(url_resolve('apple.com') == 'http://apple.com')


def test_who_is():
    resolve = url_resolve('ow.ly/i5AX30bCN5s')
    assert resolve == 'https://bitbucket.org/richardpenman/pywhois/overview'



