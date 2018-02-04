from bson.objectid import ObjectId
from flask import Flask,render_template,jsonify,json,request
from IPython.display import display_html
from bs4 import BeautifulSoup, SoupStrainer

# Import crawling functins from server.py
from server.server import *

import sys, threading
import requests
import lxml

application = Flask(__name__)

import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

@application.route("/getCouponList",methods=['POST'])
def getCouponList():
    try:
        # But we're not using a database
        #
        # coupons = db.Coupons.find()

        # Store crawled list in memory
        couponList = []
        for coupons in couponList:

            # We don't crawl here because we've stored this info in MongoDB for
            # quickest retrieval or possible downtime from crawled sites.
            couponItem = {
                    'price':coupons['price'],
                    'drugname':coupons['drugname'],
                    'storename':coupons['storename'],
                    'coupon_url':coupons['coupon_url'],
                    'id': str(coupons['_id'])
            }

            couponList.append(couponItem)
            print("Getting coupon list")
    except Exception as e:
        return str(e)
    return json.dumps(couponList)

@application.route("/submitRX",methods=['POST'])
def submitRX():
    print("SubmitRX() Called")

    try:
        json_data = request.json['info']
        rxName = json_data['rxName']

        # Call CRAWL FUNCTIONS HERE
        rx_dict = crawl_goodRx(rxName)

        for coupons in rx_dict:

            # We don't crawl here because we've stored this info in MongoDB for
            # quickest retrieval or possible downtime from crawled sites.
            couponItem = {
                    'price':coupons['price'],
                    'drugname':coupons['drugname'],
                    'storename':coupons['storename'],
                    'coupon_url':coupons['coupon_url'],
                    'id': str(coupons['_id'])
            }

            couponList.append(couponItem)

    except Exception as e:
        return str(e)
    return json.dumps(couponList)

@application.route('/')
def showCouponList():
    return render_template('index.html')

if __name__ == "__main__":
    application.run(host='0.0.0.0')
