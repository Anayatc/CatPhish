from CyberPhish import URL_Lookup


def test_add_scheme():
    assert URL_Lookup.add_scheme('ow.ly/i5AX30bCN5s' == 'http://ow.ly/i5AX30bCN5s')

