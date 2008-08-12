from gaeo.controller import BaseController
from model.core import *

class GroupController(BaseController):
    def index(self):
        self.groups = Group.all().fetch(100)
        self.message = 'Welcome!'

    def new(self):
        self.form = GroupForm(prefix="group")

    def edit(self):
        self.group=Group.get(self.params['id'])
        self.form = GroupForm(instance=self.group, prefix="group")
    
    def delete(self):
        Group.get(self.params['id']).delete()
        self.redirect('/group')
        
    def create(self):
        try:
            Group().update_attributes(self.params['group'])
            self.redirect('/group')            
        except Exception, error_text:            
            proxy=Proxy(self.params['group'])
            self.render(template = 'new', values = { 
            'group': proxy,
            'message': error_text })

    def update(self):
        try:
            Group.get(self.params['id']).update_attributes(self.params['group'])
            self.redirect('/group')
        except Exception, error_text:
            self.params['group']['key']=self.params['id']
            proxy=Proxy(self.params['group'])
            self.render(template = 'edit', values = { 
            'group': proxy,
            'message': error_text })
