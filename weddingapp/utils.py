import random
import string

import sqlite3

conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()


# Code Generator
# Creates a PIN code, to identify/secure invites
def code_generator(size=6, chars=string.digits, do_check=False):
    code = ''.join(random.choice(chars) for _ in range(size))

    def check_db():
        t = (code,)
        c.execute('SELECT * FROM weddingapp_invite WHERE code=?', t)
        c.fetchone()

        return c is None

    if do_check:
        if check_db():
            return code
        else:
            # try again
            code_generator(size, chars)
    else:
        return code

        # return ''.join(random.choice(chars) for _ in range(size))
