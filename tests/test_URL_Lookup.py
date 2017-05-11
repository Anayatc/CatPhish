from URL_Lookup import *


def test_add_scheme():
    assert(add_scheme('ow.ly/i5AX30bCN5s') == 'http://ow.ly/i5AX30bCN5s')
    assert (add_scheme('www.google.com') == 'http://www.google.com')


def test_url_resolve():
    assert(url_resolve() == 'https://bitbucket.org/richardpenman/pywhois/overview')
