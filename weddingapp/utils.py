import random
import string


# Code Generator
# Creates a PIN code, to identify/secure invites
def code_generator(size=6, chars=string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
