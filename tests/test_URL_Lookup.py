import py.test
from URL_Lookup import *


def test_add_scheme():
    assert(add_scheme('ow.ly/i5AX30bCN5s') == 'http://ow.ly/i5AX30bCN5s')
    assert(add_scheme('google.com') == 'http://google.com')
    assert(add_scheme('www.google.com') == 'http://www.google.com')
    assert(add_scheme('www.amazon.com') == 'http://www.amazon.com')
    assert(add_scheme('www.ebay.com') == 'http://www.ebay.com')
    assert(add_scheme('www.paypal.com') == 'http://www.paypal.com')
    assert(add_scheme('www.reddit.com') == 'http://www.reddit.com')
    assert(add_scheme('www.apple.com') == 'http://www.apple.com')
    assert(add_scheme('www.github.com') == 'http://www.github.com')
    assert(add_scheme('www.quora.com') == 'http://www.quora.com')
    assert(add_scheme('www.lloydsbank.com') == 'http://www.lloydsbank.com')
    assert(add_scheme('www.hsbc.com') == 'http://www.hsbc.com')
    assert(add_scheme('www.barclays.com') == 'http://www.barclays.com')
    assert(add_scheme('apple.com') == 'http://apple.com')


def test_who_is():
    resolve = add_scheme('ow.ly/i5AX30bCN5s')
    assert resolve == 'https://bitbucket.org/richardpenman/pywhois/overview'



