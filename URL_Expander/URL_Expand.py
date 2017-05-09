import requests


def url_expand(url):
    response = requests.get(url)
    if response.history:
        for resp in response.history:
            return response.status_code, resp.url
        return response.status_code, response.url
    else:
        return 'Error with url'