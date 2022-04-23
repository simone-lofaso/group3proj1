from app import myapp_obj
from flask import Flask
from flask import render_template

#This launches to the home page of the website
@myapp_obj.route('/')
def home():
    return "A Clothing Store"

