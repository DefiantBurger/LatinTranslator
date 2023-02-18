import json

import requests
from bs4 import BeautifulSoup
from flask import Blueprint, render_template, request

views = Blueprint('views', __name__)


@views.route('/', methods=['GET'])
def get_latin():
	return render_template("index.html")


@views.route('/', methods=['POST'])
def post_latin():
	post_data = json.loads(request.data.decode())
	lang = post_data[0]
	if lang == "latin":
		lang = "keyword"
	word = post_data[1]
	resp = requests.get(f"https://archives.nd.edu/cgi-bin/wordz.pl?{lang}={word}", timeout=5)
	html = resp.content.decode()
	html = html.replace("\n", "<br>")
	soup = BeautifulSoup(html, 'html.parser')

	word = soup.find('h2').text
	translation = soup.find('pre')
	translation = translation.decode_contents()

	return "idkwhattoputhere", 200, {"word": word, "translation": translation}
