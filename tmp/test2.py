class Proxy(object):
    pass
    # def __setattr__(self, name, value):
    #     self.__dict__[name] = value
    
    
p=Proxy.__dict__
# print p

o=Proxy()
o.__setattr__('kill',3)


print o.kill