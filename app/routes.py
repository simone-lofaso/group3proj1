from tkinter.tix import Form
from app import myapp_obj
from flask import Flask
from flask import render_template,flash, redirect, LoginForm, form

#This launches to the home page of the website
@myapp_obj.route('/')
def home():
    return "Welcome"
    return render_template('home.html', title = 'Sign in')

@myapp_obj.route('/login', methods=['GET', 'POST'])
def login():
    current_form  = LoginForm()
    if form.validate_on_submit ():
        flash('Login requested for user {}, remember_me={}' .format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', 
form=current_form)
