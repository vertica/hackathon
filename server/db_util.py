
from texttable import Texttable

def pretty_print_results(cur, rv):
        t = Texttable()
        colnames = [col[0] for col in cur.description]
        t.add_rows([colnames] + rv)
        print t.draw()

def make_dicts(cursor, row):
    """
        Turn query results into dictionaries keyed by column name
    """
    colnames = [col[0] for col in cursor.description]

    fmtrow = {}
    for idx, value in enumerate(row):
      fmtrow[colnames[idx]] = value

    return fmtrow

def connect_to_db():
    import vertica_python

    import re
    import os

    try:
        DB_NAME = os.environ['DB_NAME']
    except Exception, e:
        DB_NAME = 'test'

    try:
        DB_USER = os.environ['DB_USER']
    except Exception, e:
        DB_USER = 'dbadmin'

    DB_PASSWORD = ''
    DB_HOST = os.environ['DB_HOST']

    conn_info = {'host': DB_HOST,
                 'port': 5433,
                 'user': DB_USER,
                 'password': '',
                 'database': DB_NAME,
                 # 10 minutes timeout on queries
                 'read_timeout': 600,
                 # default throw error on invalid UTF-8 results
                 'unicode_error': 'strict',
                 # SSL is disabled by default
                 'ssl': False}

    db = vertica_python.connect(**conn_info)
    return db

def query_db(query, args=(), one=False, db = None, pretty_print=False):
    print "Query string: " + query
    if not db:
        db = connect_to_db()
    cur = db.cursor()

    try:
        cur.execute(query, args)
        rv = cur.fetchall()

        if rv and pretty_print:
            pretty_print_results(cur, rv)

        # Turn into colname->val dict representation of tuple
        # this isn't very efficient but will suffice for now
        rv = [make_dicts(cur, row) for row in rv]
    except Exception, e:
        print e
        rv = [{'error': e}]

    cur.close()
    return (rv[0] if rv else None) if one else rv


