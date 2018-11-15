from flask import Flask
from flask import render_template, request, redirect
from database import get_all_cats, get_cat_by_id, create_cat, delete_by_id, update_votes

app = Flask(__name__)

@app.route('/')
def catbook_home():
    cats = get_all_cats()
    return render_template("home.html", cats=cats)

@app.route('/cats/<int:cat_id>', methods=['GET','post'])
def catbook_profile(cat_id):
	if request.method == 'GET':
		cat = get_cat_by_id(cat_id)
		return render_template(
		'cat.html',cat = cat)
	else:
		update_votes(cat_id)
		return render_template(
		'cat.html',cat = cat)


@app.route('/delete/<int:cat_id>',methods = ['GET', 'POST'])
def delete(cat_id):
	if request.method == 'GET':
		return render_template('delete.html',id=cat_id)
	else:
		delete_by_id(cat_id)
		return redirect('/')


@app.route('/create', methods = ['GET', 'POST'])
def create():
	if request.method == 'GET':
		return render_template('create.html')
	else:
		cat_name = request.form['name']
		create_cat(cat_name)
		return redirect('/')

if __name__ == '__main__':
   app.run(debug = True)
