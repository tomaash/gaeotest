from gaeo.controller import BaseController
from model import core

class TestController(BaseController):
    def before_action(self):
        """docstring for before_action"""
        if 1==2: self.redirect('/') 
             
    def cau(self):
        #users = core.User.all().fetch(1000)
        # user=core.User(name="tom",email="sd")
        # user.put()
        self.message = "debile!"
        self.render(template = 'index',values = { 
       'message': 'hello', 
       'users': core.User.all().fetch(1000) #users 
         } )
         
        
