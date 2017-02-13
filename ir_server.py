#!/usr/bin/python
from bottle import post, route, request, run
import os
@route('/')
@route('/', method='POST')
def release_control():
    if (request.POST.get("power")):
        os.system("irsend SEND_ONCE 3100 KEY_POWER")
    if (request.POST.get("1")):
    	os.system("irsend SEND_ONCE 3100 KEY_1")
    if (request.POST.get("2")):
    	os.system("irsend SEND_ONCE 3100 KEY_2")
    if (request.POST.get("3")):
    	os.system("irsend SEND_ONCE 3100 KEY_3")
    if (request.POST.get("4")):
    	os.system("irsend SEND_ONCE 3100 KEY_4")
    if (request.POST.get("5")):
    	os.system("irsend SEND_ONCE 3100 KEY_5")
    if (request.POST.get("6")):
    	os.system("irsend SEND_ONCE 3100 KEY_6")
    if (request.POST.get("7")):
    	os.system("irsend SEND_ONCE 3100 KEY_7")
    if (request.POST.get("8")):
    	os.system("irsend SEND_ONCE 3100 KEY_8")
    if (request.POST.get("9")):
    	os.system("irsend SEND_ONCE 3100 KEY_9")
    if (request.POST.get("0")):
    	os.system("irsend SEND_ONCE 3100 KEY_0")
    if (request.POST.get("TLC")):
    	os.system("/home/pi/tlc.sh")
    if (request.POST.get("0")):
    	os.system("irsend SEND_ONCE 3100 KEY_0")
    if (request.POST.get("DISC")):
    	os.system("/home/pi/discovery.sh")
    if (request.POST.get("SCI")):
    	os.system("/home/pi/sci.sh")
    if (request.POST.get("TOON")):
    	os.system("/home/pi/number.sh 5 6 4")
    if (request.POST.get("HIST")):
    	os.system("/home/pi/number.sh 5 2 2")
    if (request.POST.get("ANIMAL")):
    	os.system("/home/pi/number.sh 5 2 5")
    if (request.POST.get("GEO")):
    	os.system("/home/pi/number.sh 5 2 4")
    if (request.POST.get("FOOD")):
    	os.system("/home/pi/number.sh 6 0 3")
    if (request.POST.get("CMDY")):
    	os.system("/home/pi/number.sh 6 2 5")
    return """
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <form method="POST" action="/">
    <div id="content">
    <p><input id="submit" name="power" type="submit" value="Power"></p>
    <input id="submit" name="1" value="1" type="submit">
    <input id="submit" name="2" value="2" type="submit">
    <input id="submit" name="3" value="3" type="submit">
    </p><p>
    <input id="submit" name="4" value="4" type="submit">
    <input id="submit" name="5" value="5" type="submit">
    <input id="submit" name="6" value="6" type="submit">
    </p><p>
    <input id="submit" name="7" value="7" type="submit">
    <input id="submit" name="8" value="8" type="submit">
    <input id="submit" name="9" value="9" type="submit">
    </p><p>
    <input id="submit" name="0" value="0" type="submit">
    </p><p>
    <input id="submit" name="TLC" value="TLC" type="submit">
    <input id="submit" name="DISC" value="DISC" type="submit">
    <input id="submit" name="SCI" value="SCI" type="submit">
    </p><p>
    <input id="submit" name="TOON" value="TOON" type="submit">
    <input id="submit" name="HIST" value="HIST" type="submit">
    <input id="submit" name="ANIMAL" value="ANIMAL" type="submit">
    </p><p>
    <input id="submit" name="GEO" value="GEO" type="submit">
    <input id="submit" name="FOOD" value="FOOD" type="submit">
    <input id="submit" name="CMDY" value="CMDY" type="submit">
    </form></div>
    <style>
        body {
	background-color: #000;
        font: 15px/25px 'Fira Sans', sans-serif;
        }
        #content {
        margin: 0px auto;
        text-align: center;
        }
        #submit {
        width: 4em;  height: 2em;
        background: rgb(66, 184, 66);
        border-radius: 4px;
        color: #000;
        font-family: 'Fira Sans', sans-serif;
        font-size: 25px;
        font-weight: 900;
        text-shadow: 0 1px 1px rgba(0, 0, 0, 0.2);
        letter-spacing: 3px;
        border:none;
        }
    </style>
    """
run(host="0.0.0.0",port=8080, debug=False)
