from google.appengine.ext import db
from gaeo.model import BaseModel
from google.appengine.ext.db.djangoforms import *

class Proxy(object):
    def __init__(self,user_data):
        for key in user_data:
            self.__setattr__(key,user_data[key])

class User(BaseModel): 
    first_name = db.StringProperty()
    last_name = db.StringProperty()
    password = db.StringProperty()
    email = db.EmailProperty()

    def name(self):
        return self.first_name+" "+self.last_name

    def __unicode__(self):
        return self.first_name+" "+self.last_name


class Group(BaseModel):
  name = db.StringProperty()
  description = db.TextProperty()

  @property
  def members(self):
    return Contact.gql("WHERE groups = :1", self.key())

ROLES = (
  # value, label
  ('a',"role a"),
  ('b',"role b"),
  ('c',"role c")
)

listgroups = map(lambda x: (x.key(),x.name),Group().all().fetch(100))
#print listgroups

class Contact(BaseModel):
  # User that owns this entry.
  # owner = db.UserProperty()
  owner = db.ReferenceProperty(User, required=False, collection_name='companies')

  # Basic info.
  name = db.StringProperty()
  birth_day = db.DateProperty()

  # Address info.
  address = db.PostalAddressProperty()
  roles  = db.StringListProperty()

  # The original organization properties have been replaced by
  # an implicitly created property called 'companies'. 

  # Group affiliation
  groups = db.ListProperty(db.Key)

class ContactForm(ModelForm):
  roles = forms.CharField(widget=forms.CheckboxSelectMultiple(choices=ROLES))
  groups = forms.CharField(widget=forms.CheckboxSelectMultiple(choices=listgroups))
  class Meta:
    model = Contact

class GroupForm(ModelForm):
  class Meta:
    model = Group

class Company(BaseModel):
  name = db.StringProperty()
  description = db.StringProperty()
  company_address = db.PostalAddressProperty()

class ContactCompany(BaseModel):
  contact = db.ReferenceProperty(Contact,
                                 required=True,
                                 collection_name='companies')
  company = db.ReferenceProperty(Company,
                                 required=True,
                                 collection_name='contacts')
  title = db.StringProperty()