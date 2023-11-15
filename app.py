from flask import Flask, request

from run import send_email

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/send_mail", methods=['POST'])
def send_mail():
    receiver = request.form['receiver']
    subject = request.form['subject']
    url = request.form['url']
    return send_email(receiver, subject, url)

if __name__=='__main__':
    app.run("0.0.0.0")
