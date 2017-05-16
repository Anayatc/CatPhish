from flask import Flask, render_template, request
from URL_Lookup import *

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/send", methods=['GET', 'POST'])
def send():

    if request.method == 'POST':
        start_url = request.form['start_URL']
        url_resolve(start_url)
        domain_name()
        final = who_is()
        print(final)

        return render_template("send.html", final=final)

        # return render_template("send.html")

    else:
        return render_template("index.html")


def url():
    start_url = request.form['start_URL']
    return start_url

if __name__ == "__main__":
    app.run()
