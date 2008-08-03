from google.appengine.ext import db
from gaeo.model import BaseModel

class Proxy(object):
    def __init__(self,user_data):
        for key in user_data:
            self.__setattr__(key,user_data[key])

class User(BaseModel): 
    first_name = db.StringProperty(required=False)
    last_name = db.StringProperty(required=False)
    password = db.StringProperty(required=False)
    email = db.EmailProperty(required=False)
