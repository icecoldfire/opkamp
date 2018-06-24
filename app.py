#!/usr/bin/python3
# -*- coding: utf-8 -*-

import base64
import io

from Banner import Banner
from flask import Flask, render_template, request, make_response
from datetime import datetime
app = Flask(__name__)

files = {'1': 'img/1.jpg',
 '2': 'img/2.jpg',
 '3': 'img/3.jpg',
 '4': 'img/4.png',
 '5': 'img/5.png',
 '6': 'img/6.png',
 '7': 'img/7.png',
 '8': 'img/8.jpg',
 '9': 'img/9.jpg',
 '10': 'img/10.jpg',
 '11': 'img/11.jpg',
 '12': 'img/12.jpg'}
 
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    tekst = request.form["tekst"]
    image = request.form["image"]
    banner = Banner(files[image], tekst)
    banner.schrijf()
    imgByteArr = io.BytesIO()
    banner.get_image().save(imgByteArr, format='JPEG')
    imgByteArr = imgByteArr.getvalue()
    response = make_response(imgByteArr)
    response.headers.set('Content-Type', 'image/jpeg')
    response.headers.set('Content-Disposition', 'attachment', filename='banner.jpg')
    return response

@app.route('/generate/base64', methods=['POST'])
def generateBase64():
    tekst = request.form["tekst"]
    image = request.form["image"]
    banner = Banner(files[image], tekst)
    banner.schrijf()
    imgByteArr = io.BytesIO()
    banner.get_image().save(imgByteArr, format='JPEG')
    imgByteArr = imgByteArr.getvalue()
    data_uri = base64.b64encode(imgByteArr).decode('utf-8').replace('\n', '')
    img_tag = '<img src="data:image/jpeg;base64,{0}">'.format(data_uri)
    result = "Content-Type: text/html;charset=utf-8\n\n\n\n"
    result = img_tag
    return result

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

