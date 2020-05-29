import os
import string
import sqlite3
from math import floor
from linkmon import app
from sqlite3 import OperationalError
from flask import request, redirect, render_template
try:
    from urllib.parse import urlparse  
    str_encode = str.encode
except ImportError:
    from urlparse import urlparse  
    str_encode = str




@app.route('/health', methods=['GET'])
def health_check():
    """
    To check if the server is up or not
    """
    return "O.K", 200


host = app.config['HOST']

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        actual_url = str_encode(request.form.get('act_url'))
        custom_route = str_encode(request.form.get('custom_url'))
        if urlparse(actual_url).scheme == '':
            url = 'http://' + actual_url
        else:
            url = actual_url
            with sqlite3.connect('database/urls.db') as conn:
                cursor = conn.cursor()
                res = cursor.execute(
                    'INSERT INTO STORE_URL (ACT_URL, CUSTOM_URL) VALUES (?, ?)',
                    [actual_url, custom_route]
                )
                conn.commit()
        return render_template('index.html', custom_url=host + custom_route)
        
    return render_template('index.html')


@app.route('/<custom_route>')
def redirect_short_url(custom_route):
    custom_route = custom_route
    url = host  
    try: 
        with sqlite3.connect('database/urls.db') as conn:
            cursor = conn.cursor()
            res = cursor.execute('SELECT ACT_URL FROM STORE_URL WHERE CUSTOM_URL=?', [custom_route])
            try:
                url = res.fetchone()
                if url is not None:
                    url = url[0]
            except Exception as e:
                print(e)
        return redirect(url)

    except OverflowError as e:
        return str(e)

