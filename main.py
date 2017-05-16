from flask import Flask, render_template, request
import requests
from urllib.parse import  urlparse

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/send/>", methods=['GET', 'POST'])
start_url = request.form['start_URL']
def add_scheme(url):
    if url.startswith('http://') or url.startswith('https://'):
        return url
    if url.startswith('www.'):
        return 'http://' + url
    else :
        return 'http://' + url


def send():
    if request.method == 'POST':

        return render_template("send.html")

        # return render_template("send.html")

    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run()
