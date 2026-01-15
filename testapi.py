import hmac
import hashlib
import base64
import os
from dotenv import load_dotenv
from flask import Flask
load_dotenv()
app_id = os.getenv("APP_ID")
raw_key = os.getenv("APP_KEY")
app = Flask(__name__)
@ app.route('/login')
def login():
    dict = {'version': '0.5', 'appID': app_id,'RedirectURL': 'http://127.0.0.1:5000/login'}
    sorted_dict = dict(sorted(dict.items()))
    message = '&'.join([f"{key}={value}" for key, value in sorted_dict.items()])
    key = raw_key.encode('utf-8')
    signature = hmac.new(key, message.encode('utf-8'), hashlib.sha1).digest()
    signature_base64 = base64.b64encode(signature).decode('utf-8')
    return signature_base64


if __name__ == '__main__':
    app.run()
