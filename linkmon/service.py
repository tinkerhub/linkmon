import os
import sqlite3
from linkmon import app
from flask import request, redirect

@app.route('/health', methods=['GET'])
def health_check():
    """
    To check if the server is up or not
    """
    return "O.K", 200

