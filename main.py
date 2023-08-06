from flask import Flask, render_template, request
import requests


app = Flask(__name__)

PRIVATE_API_KEY = "PRIVATE_API_KEY"

@app.route('/', methods=['GET', 'POST'])
def home_page():
	if request.method == "POST":
		data = request.form
		name = data["name"]
		email = data["email"]
		message = data["message"]
		send_simple_message(name, email, message)

		return render_template("index.html", msg_sent=True)
	return render_template("index.html", msg_sent=False)

def send_simple_message(name, email, message):

	return requests.post(
	    "https://api.mailgun.net/v3/sandbox6e4ed74c61c14ff1950555ac88ad0042.mailgun.org/messages",
		auth=("api", PRIVATE_API_KEY),
		data={"from": "Mailgun Sandbox <postmaster@sandbox6e4ed74c61c14ff1950555ac88ad0042.mailgun.org>",
			"to": "Leandro <lele.alvarez86@gmail.com>",
			"subject": "New Profile Projects website message",
			"text": f"Name:{name}\nEmail:{email}\nMessage:{message}"})











if __name__ == "__main__":
    app.run(debug=True)