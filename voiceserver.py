import requests
from flask import Flask, session, redirect, url_for, escape, request

app = Flask(__name__)

@app.route('/')
def index():
    return '''Voice Server'''


zonemap = [ ["all", "house", "cornhole", 'whole'],
            ['living room'],
            ["kitchen"],
            ["living room lamp", "back lamp"],
            ["front", "entry"],
            ["office"],
            ["hall"],
            ["left", "my lamp", "wills"],
            ["right", "sarah", "sarahs"],
            ["master", "our", "bedroom"]]

@app.route('/av/<com>')
def autovoice(com):
   if not len(com):
      print( "Empty Request")
      return ""
   zone = '-1'
   level = '1'
   resp = "None"
   
   for z in reversed(range(len(zonemap))):
      for zoneName in zonemap[z]:
         if zoneName in com:
            print( "Found zone: " + zoneName)
            zone = str(z)
            break
      if not zone == '-1':
         break
      
   if 'on' in com:
      level = '1'
   elif 'night' in com or 'dim' in com or 'them' in com:
      level = '2'
   elif 'off' in com:
      level = '0'
   
   if zone != '-1':
      url = 'http://kale:2000/zone/' + zone + '/' +  level
      print(com + ":" + url)
      resp = requests.get(url).content
   else:
      print("No Zone Found")

   return resp
      



# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
app.run(host='0.0.0.0', debug=True, port=2004)

