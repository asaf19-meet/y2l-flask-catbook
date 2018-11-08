from flask import Flask
from flask import render_template
from database import get_all_cats, get_cat_by_id

app = Flask(__name__)

@app.route('/')
def catbook_home():
    cats = get_all_cats()
    return render_template("home.html", cats=cats)

@app.route('/cats/<int:cat_id>')
def catbook_profile(cat_id):
	cat = get_cat_by_id(cat_id)
	return render_template(
		'cat.html',cat = cat)

if __name__ == '__main__':
   app.run(debug = True)
