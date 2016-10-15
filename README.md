# Hackathon
This is a getting started kit for Hackathons using Vertica!

First clone the repo with:

    git clone git@github.com:vertica/hackathon.git vertica-hackathon
    
    cd vertica-hackathon

Run your demo server that submits a select 1 query:

    cd server
    export FLASK_DEBUG=1 # Run flask in debug mode
    python server.py
    
Visit localhost:5000 to see the Hello World page!
