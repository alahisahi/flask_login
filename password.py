'''
from flask_bcrypt import Bcrypt
from  flask import Flask
#from flask.ext.bcrypt import Bcrypt

bcrypt=Bcrypt()

password='superdatascience'

hashed_password=bcrypt.generate_password_hash(password=password)
print(hashed_password)

check=bcrypt.check_password_hash(hashed_password,'wrongpassword')
print(check)
'''
from werkzeug.security import generate_password_hash,check_password_hash
hashpass=generate_password_hash('mypassword')
print(hashpass)

check=check_password_hash(hashpass,'wrsjbfjsbf')
print(check)
