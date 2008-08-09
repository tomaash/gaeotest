from gaeo.controller import BaseController
from model.core import *
import time
import datetime

class ContactController(BaseController):
    def index(self):
        self.contacts = Contact.all().fetch(100)
        self.message = 'Welcome!'

    # def bootstrap(self):
    #     usr=User.all().get()
    #     Contact().update_attributes({"owner": usr, "name": "test", "birth_day": datetime.date.today(), "address": "ulice 1"})        
    #     # Contact().update_attributes(owner=usr, name="test", birth_day="123", address="ulice 1")        
    #     self.redirect('/')
    
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
        date_array=self.params['contact']['birth_day'].split('-')
        self.params['contact']['birth_day']=datetime.date(int(date_array[0]),int(date_array[1]),int(date_array[2]))
    
    def __prefixize_params(self):
        for key, value in self.params['contact'].items():
            self.params['contact']["contact-"+key]=value
        
    def create(self):
        try:
            self.__sanitize_params()
            Contact().update_attributes(self.params['contact'])
            self.redirect('/contact')
        except Exception, error_text:            
            self.__prefixize_params()
            self.render(template = 'new', values = {             
            'form': ContactForm(self.params['contact'],prefix="contact"),
            # 'message': self.params['contact'],
            'error': error_text
            })
    
    def update(self):
        try:
            self.__sanitize_params()
            Contact.get(self.params['id']).update_attributes(self.params['contact'])
            self.redirect('/contact')
        except Exception, error_text:
            self.__prefixize_params()
            self.params['contact']['key']=self.params['id']
            self.render(template = 'edit', values = { 
            'form': ContactForm(self.params['contact'],prefix="contact"),
            'error': error_text })

