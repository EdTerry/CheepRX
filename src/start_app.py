from bson.objectid import ObjectId
from flask import Flask,render_template,jsonify,json,request
from IPython.display import display_html
from bs4 import BeautifulSoup, SoupStrainer

import sys, threading
import requests
import lxml

application = Flask(__name__)

import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

@application.route('/')
def showPrice():
    print("application running")
    return render_template('index.html')

if __name__ == "__main__":
    application.run(host='0.0.0.0')
