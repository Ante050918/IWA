#!python.exe

import db
import password_utils

def register(username, email, password):
    user = db.create_user(username, email, password)
    if user:
        return True
    else:
        return False
        
def login(ime, password):
    user = db.get_user(ime)
    if (user and password_utils.verify_password(password, user[3])):
        return True, user[0]
    else:
        return False, None
        
def change_password(ime, old, new, new2):
    user = db.get_user(ime)
    if (password_utils.verify_password(old, user[3]) and new==new2):
        success = db.change_user_password(ime, new)
        if success:
            return True
        else:
            return False