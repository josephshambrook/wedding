from sqlite3 import dbapi2 as sqlite


def unlock_db(db_filename):
    """Replace db_filename with the name of the SQLite database."""
    connection = sqlite.connect(db_filename)
    connection.commit()
    connection.close()

unlock_db("db.sqlite3")