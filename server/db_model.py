"""
    Connect to a vertica database
"""
from flask import g
import hp_vertica_client
import re

DB_NAME = 'test'
DB_USER = 'dbadmin'
DB_PASSWORD = ''
DB_HOST = 'ec2-54-236-111-135.compute-1.amazonaws.com'

def make_dicts(cursor, row):
    """
        Turn query results into dictionaries keyed by column name
    """
    colnames = [col[0] for col in cursor.description]

    fmtrow = {}
    for idx, value in enumerate(row):
      fmtrow[colnames[idx]] = value

    return fmtrow

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = hp_vertica_client.connect(database=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
    return db


def query_db(query, args=(), one=False):
    print query
    cur = get_db().cursor()

    try:
        cur.execute(query, args)
        rv = cur.fetchall()

        # Turn into colname->val dict representation of tuple
        # this isn't very efficient but will suffice for now
        rv = [make_dicts(cur, row) for row in rv]
    except Exception, e:
        print e
        rv = [{'error': e}]

    cur.close()
    return (rv[0] if rv else None) if one else rv

def select_one():
    """
        Select 1 from database
    """
    sql = "select 1"
    results = query_db(sql)
    print results
    return results

# @app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
