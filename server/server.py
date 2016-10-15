import os
import sys
sys.path.append(os.getcwd() + "/deps")


from flask import Flask
from flask import render_template

app = Flask(__name__)

import db_model as db
import json

from datetime import date
from datetime import timedelta

@app.route("/")
def index():

    results = db.select_one()

    return render_template("index.html")

if __name__ == "__main__":
    app.run('0.0.0.0')
