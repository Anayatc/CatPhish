from flask import Flask, render_template, request
from URL_Lookup import *

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/send", methods=['GET', 'POST'])
def user_url():
    start_url = request.form['start_URL']
    return start_url


def send():
    if request.method == 'POST':

        add_scheme(user_url)
        url_resolve()
        domain_name()
        final = who_is()
        print(final)
        return render_template("send.html")

        # return render_template("send.html")

    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run()
