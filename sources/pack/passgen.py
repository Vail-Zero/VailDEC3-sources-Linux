# pass_gen.py
import string
import secrets
import os

def gen(size=12):
   chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
   # 記号を含める場合
   chars += '#$?!%_'
   return ''.join(secrets.choice(chars) for x in range(size))
