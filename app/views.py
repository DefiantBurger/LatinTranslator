import json

import requests
from bs4 import BeautifulSoup
from flask import Blueprint, render_template, request

pos_to_full = {
	"N": "noun",
	"V": "verb",
	"ADJ": "adjective",
	"PREP": "preposition"
}

views = Blueprint('views', __name__)


@views.route('/', methods=['GET'])
def get_latin():
	return render_template("index.html")


@views.route('/', methods=['POST'])
def post_latin():
	post_data = json.loads(request.data.decode())
	lang = post_data[0]
	if lang != "latin":
		return "idkwhattoputhere", 200, {"word": "Error", "translation": "-----English-To-Latin translation is temporarily disabled, sorry."}
	word = post_data[1]
	translation = requests.get(f"https://latin-words.com/cgi-bin/translate.cgi?query={word}", timeout=5).json()["message"]
	translation = translation.replace("\n", "<br>").replace("\r", "")

	# parts = []
	# lines = list(filter(None, translation.split("<br/>")))
	# for ln in lines:
	# 	matches = re.findall(r"(?<!\S)[A-Z]+(?!\S)", ln)
	# 	if matches:
	# 		parts.append(matches[0])
	#
	# parts = sorted(list(set(parts)))
	#
	# checked_parts = []
	# for part in parts:
	# 	code = requests.head(f"http://latindictionary.wikidot.com/{pos_to_full[part]}:{word}").status_code
	# 	print(code)
	# 	if code == 404:
	# 		checked_parts.append(f"{part}=0")
	# 	else:
	# 		checked_parts.append(f"{part}=1")

	return "idkwhattoputhere", 200, {"word": word, "translation": translation}


@views.route('/report-issue')
def report_issue():
	pass
