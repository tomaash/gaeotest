params={u'user[password]': u'sdfgsdfgsdfg', 'controller': 'user', u'user[last_name]': u'sdfgsdfg', u'user[email]': u'sdfgsdfg', 'action': 'create', u'save': u'Save', u'user[first_name]': u'dsfgsdfg'} 

def appender(dict,arr,val):
        if len(arr) > 1:
            try:
                dict[arr[0]]
            except KeyError:
                dict[arr[0]]={}
            return {arr[0]: appender(dict[arr[0]],arr[1:],val)}
        else:
            dict[arr[0]]=val
            return 

def nested_params(prm):
    prm2={}
    for param in prm:
        parray = param.replace(']',"").split('[')
        appender(prm2,parray,prm[param])
    return prm2

print nested_params(params)
