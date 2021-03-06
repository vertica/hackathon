from db_util import *
import readline

if __name__ == "__main__":
    import sys
    db = connect_to_db()

    print "Welcome to the mini Vertica client! Enter your queries or type '\\q' to quit"
    line = raw_input("> ")
    while not line.strip() == "\\q":
        if len(line):
            while not line[-1] == ";":
                line += raw_input("(cont)> ")
            if line.split(' ')[0] == "insert":
                line += "; commit;"
            if line.split(' ')[0] == "copy":
                # Use cur.copy instead of cur.execute for loading files
                load_db(line)
            else:
                query_db(line, pretty_print=True)
        line = raw_input("> ")

