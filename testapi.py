import hmac
import hashlib
import base64
import os
from dotenv import load_dotenv
from flask import Flask, redirect, request, session
load_dotenv()
app_id = os.getenv("APP_ID")
raw_key = os.getenv("APP_KEY")
app = Flask(__name__)
app.config['SECRET_KEY'] = '123456789'
@ app.route('/login')
def login():
    dic = {'version': '0.5', 'appID': app_id,'RedirectURL': 'http://127.0.0.1:5000/login'}
    sorted_dict = dict(sorted(dic.items()))
    message = '&'.join([f"{key}={value}" for key, value in sorted_dict.items()])
    key = raw_key.encode('utf-8')
    signature = hmac.new(key, message.encode('utf-8'), hashlib.sha1).digest()
    signature_base64 = base64.b64encode(signature).decode('utf-8')
    url = "https://wwwtest.einvoice.nat.gov.tw/accounts/login/mw?login_challenge=26bf3bf5d3d14d4da76929add91ab499"
    login_url = f"{url}?{message}&signature={signature_base64}"
    return redirect(login_url)
@ app.route('/back')
def back():
    card_no = request.args.get('cardNo')
    token = request.args.get('token')

    if card_no and token:
        session['cardNo'] = card_no
        session['token'] = token
        return f"拿到載具 {card_no} 了！接下來我們可以去抓發票做地圖了。"
    
    return "沒拿到資料，登入失敗。", 400
if __name__ == '__main__':
    app.run(debug=True)
