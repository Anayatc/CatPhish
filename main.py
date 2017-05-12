from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/send", methods=['GET', 'POST'])
def send():

    if request.method == 'POST':
        short_url = request.form['start_URL']
        print(short_url)
        return render_template("send.html")

    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run()
