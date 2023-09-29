#!/usr/bin/python3
# -*- coding: utf-8 -*-

import base64
import io

from Banner import Banner
import cgitb
import cgi

cgitb.enable()
form = cgi.FieldStorage()



try:
    tekst = form["tekst"].value
except KeyError:
    tekst = ""
try:
    image = form["image"].value
except KeyError:
    image = "1.jpg"

banner = Banner("img\\" + image, (487, 55), (720, 170), tekst)
banner.schrijf()
imgByteArr = io.BytesIO()
banner.get_image().save(imgByteArr, format='JPEG')
imgByteArr = imgByteArr.getvalue()
data_uri = base64.b64encode(imgByteArr).decode('utf-8').replace('\n', '')
img_tag = '<img src="data:image/jpeg;base64,{0}">'.format(data_uri)
print("Content-Type: text/html;charset=utf-8\n\n\n\n")
print(img_tag)
