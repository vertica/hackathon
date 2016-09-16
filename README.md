# Hackathon
A getting started kit for Hackathons using Vertica!

## Install the vertica python client
First you need to install the vertica python client, so that you can connect to the database through your python code.

If you are using pip >= 1.4 and you don't already have pytz installed:
    pip install --pre pytz
    
To install vertica-python with pip:

    pip install vertica-python

To install vertica-python with pip (with optional namedparams dependencies):
    pip install 'vertica-python[namedparams]'

More instructions and source code at: https://github.com/uber/vertica-python

## Install Flask, a python framework and submit your first query

Flask is a powerfull and lightweight python framework. You can install it with:

    pip install flask

Run your demo server that submits a select 1 query

    python server.py
    
Visit localhost:5000 to see the Hello World page.
