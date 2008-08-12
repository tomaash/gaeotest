from gaeo.controller import BaseController
from model.core import *
import time
import datetime
import logging

class ContactController(BaseController):
    def index(self):
        self.contacts = Contact.all().fetch(100)
        self.message = 'Welcome!'
        listgroups = map(lambda x: (x.key(),x.name),Group().all().fetch(100))
        # print listgroups
        # print Group.all().get().key()
        

    def bootstrap(self):
          usr=User.all().get()
          cnt=Contact().all().get()
#          Contact().update_attributes({"owner": usr, "name": "test", "birth_day": datetime.date.today(), "address": "ulice 1"})
          Group().update_attributes({"name": "newgroup", "description": "tasdfasdgest"})        
          # Contact().update_attributes(owner=usr, name="test", birth_day="123", address="ulice 1")        

          # print groups
          #self.redirect('/')
    
    def new(self):
        self.form = ContactForm({"contact-birth_day": datetime.date.today()}, prefix="contact")

    def edit(self):
        self.contact=Contact.get(self.params['id'])
        self.form = ContactForm(instance=self.contact, prefix="contact")
    
    def delete(self):
        Contact.get(self.params['id']).delete()
        self.redirect('/contact')

    def __sanitize_params(self):
        mykey=User.get(self.params['contact']['owner']).key()
        self.params['contact']['owner']=mykey
        
        # logging.info(type(self.params['contact']['birth_day']))
        # logging.info(type(""))
        if type(self.params['contact']['birth_day'])==type(u''):
            date_array=self.params['contact']['birth_day'].split('-')
            self.params['contact']['birth_day']=datetime.date(int(date_array[0]),int(date_array[1]),int(date_array[2]))
        
        if self.params['contact'].has_key('roles'):
            roles = self.params['contact']['roles']
        else:
            roles = []
            
        if self.params['contact'].has_key('groups'):
            groups = self.params['contact']['groups']
        else: 
            groups = []
        
        if type(roles)!=type([]):
            roles=[roles] 
        if type(groups)!=type([]):
            groups=[groups] 
        
        new_group_array = map(lambda x: Group.get(x).key(), groups)
        self.params['contact']['groups']=new_group_array
        self.params['contact']['roles']=roles

    
    def __prefixize_params(self):
        for key, value in self.params['contact'].items():
            self.params['contact']["contact-"+key]=value
        
    def create(self):
        try:
            self.__sanitize_params()
            Contact().update_attributes(self.params['contact'])
            self.redirect('/contact')
        except Exception, error_text:            
            self.__sanitize_params()
            self.__prefixize_params()
            self.render(template = 'new', values = {             
            'form': ContactForm(self.params['contact'],prefix="contact"),
            'contact': Proxy(self.params['contact']),
            'error': error_text,
            'message': self.params
            })
    
    def update(self):
        try:
            self.__sanitize_params()
            Contact.get(self.params['id']).update_attributes(self.params['contact'])
            self.redirect('/contact')
        except Exception, error_text:
            self.__sanitize_params()
            self.__prefixize_params()
#            self.params['contact']['key']=self.params['id']
            self.render(template = 'edit', values = { 
            'form': ContactForm(self.params['contact'],prefix="contact"),
            'contact': Contact.get(self.params['id']),
            'error': error_text,
            'message': self.params })

