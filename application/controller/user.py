from gaeo.controller import BaseController
from model.core import *

class UserController(BaseController):
    def index(self):
        self.users = User.all().fetch(100)
        self.message = 'Welcome!'

    def new(self):
        pass        

    def edit(self):
        self.user=User.get(self.params['id'])
    
    def delete(self):
        User.get(self.params['id']).delete()
        self.redirect('/user')
        
    def create(self):
        try:
            User().update_attributes(self.params['user'])
            self.redirect('/user')            
        except Exception, error_text:            
            proxy_user=Proxy(self.params['user'])
            self.render(template = 'new', values = { 
            'user': proxy_user,
            'message': error_text })

    def update(self):
        try:
            User.get(self.params['id']).update_attributes(self.params['user'])
            self.redirect('/user')
        except Exception, error_text:
            self.params['user']['key']=self.params['id']
            proxy_user=Proxy(self.params['user'])
            self.render(template = 'edit', values = { 
            'user': proxy_user,
            'message': error_text })
        
