import pytest
from werkzeug.security import check_password_hash
from models import User

def test_setget_password():
    """
    GIVEN a User model 
    WHEN set_password is called with a password and is passed to check_password
    THEN the password should be the original string before hashing
    """
    user = User()
    pwd = "pass&WoRd"
    hash = user.set_password(pwd)
    assert check_password_hash(hash, pwd)
    # pwd = "pass WoRD"
    # hash = User.set_password(pwd)
    # assert check_password_hash(hash, pwd) == True