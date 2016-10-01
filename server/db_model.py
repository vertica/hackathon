"""
    Connect to a vertica database and run queries
"""
from flask import g
from cli import *

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = connect_to_db()
    return db

def select_one():
    """
        Select 1 from database
    """
    sql = "SELECT 1"
    results = query_db(sql, db = get_db(), pretty_print=True)
    return results

# @app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
