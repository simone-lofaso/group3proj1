from app import myapp_obj
from flask import Flask
from flask import render_template
from flask import request
from app.forms import SearchForm

#This launches to the home page of the website
@myapp_obj.route('/', methods = ['POST', 'GET'])
def home():
    form = SearchForm()
    if form.validate_on_submit() and request.method == 'POST':
        return SearchPage()
    return render_template('home.html',form = form)

@myapp_obj.route('/SearchResults')
def SearchPage():
    return render_template('results.html')
