from flask import Flask, render_template, request
from URL_Lookup import *

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/send", methods=['GET', 'POST'])
def send():

    if request.method == 'POST':
        short_url = request.form['start_URL']
        add_scheme(short_url)
        url_resolve()
        domain_name()
        return who_is()

        # return render_template("send.html")

    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run()
