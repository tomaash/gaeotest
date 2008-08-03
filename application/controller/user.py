from gaeo.controller import BaseController
from model.core import *

class UserController(BaseController):
    def index(self):
        self.users = User.all().fetch(100)
        self.message = 'hellokity'

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
        except:            
            proxy_user=Proxy(self.params['user'])
            self.render(template = 'new', values = { 
            'user': proxy_user })

    def update(self):
        try:
            User.get(self.params['id']).update_attributes(self.params['user'])
            self.redirect('/user')
        except:
            self.params['user']['key']=self.params['id']
            proxy_user=Proxy(self.params['user'])
            self.render(template = 'edit', values = { 
            'user': proxy_user })
        
