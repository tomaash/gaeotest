from google.appengine.ext import db
from gaeo.model import BaseModel

class Proxy(object):
    def __init__(self,user_data):
        for key in user_data:
            self.__setattr__(key,user_data[key])

class User(BaseModel): 
    first_name = db.StringProperty()
    last_name = db.StringProperty()
    password = db.StringProperty()
    email = db.EmailProperty()
