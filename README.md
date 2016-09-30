# Hackathon
This is a getting started kit for Hackathons using Vertica!

## Install the vertica python client
First you need to install the vertica python client, so that you can connect to the database by simply writing python code.

There are a few requirements for that. First, you need to install pip. If you are using Python 2 >=2.7.9 or Python 3 >=3.4 downloaded from python.org you will already have pip. Otherwise follow installation instructions here: https://pip.pypa.io/en/stable/installing/

If you are using pip >= 1.4 and you don't already have pytz installed:
    pip install --pre pytz
    
To install vertica-python with pip run the following command with sudo priviledges:

    sudo pip install vertica-python

You will get a prompt to enter your password. Enter your password and hit enter.

More instructions and source code of the python client at: https://github.com/uber/vertica-python

## Install Flask, a python framework and submit your first query

Flask is a powerfull and lightweight python framework. It does all the dirty work of setting up a server. You can install it with:

    pip install flask

Run your demo server that submits a select 1 query:

    python server.py
    
Visit localhost:5000 to see the Hello World page.
