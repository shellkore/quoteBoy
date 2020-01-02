from flask import Flask, render_template, request, jsonify
from quoter import quoteLister
import random

app = Flask(__name__)

@app.route('/')
def success():
	return render_template("home.html")

@app.route('/quote', methods =['GET'])
def get_quote():
	tag = request.args['tag']
	currentQuoteList = quoteLister(tag)
	currentQuote = random.choice(currentQuoteList).strip()
	return jsonify({'quote': currentQuote})


if __name__ == '__main__':
   app.run(debug = True, port = 5000)