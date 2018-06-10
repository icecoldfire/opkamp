#!/usr/bin/python3
# -*- coding: utf-8 -*-

import base64
import io

from Banner import Banner
from flask import Flask, render_template, request
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['GET', 'POST'])
def generate():
    tekst = request.form["tekst"]
    image = request.form["image"]
    banner = Banner("img/" + image, tekst)
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

