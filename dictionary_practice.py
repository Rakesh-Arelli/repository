'''d={'a':12,'b':22,'c':33,'d':44}
print(type(d))

op:
{'a': 12, 'b': 22, 'c': 33, 'd': 44}
<class 'dict'>

'''
'''
data={}
data["dhoni"]=183
data["sachin"]=200
data["rohit"]=264
print(data)

op:{'dhoni': 183, 'sachin': 200, 'rohit': 264}
'''
'''
data1={'id':22222,'name':"Rakesh",'desg':"Developer"}
data2={'id':22134,'name':"Harish",'desg':"tester"}
##print(data1['name'])
##print(data1['id'])
##op:Rakesh
##22222
data1['desg']="Python Trainee"
data2['salary']=50000
print(data1)
print(data2)
##op:
##{'id': 22222, 'name': 'Rakesh', 'desg': 'Python Trainee'}
##{'id': 22134, 'name': 'Harish', 'desg': 'tester', 'salary': 50000}
##  deltion:del stmt is used for perfoming deletion operation.
#syn:del[key]


del data2['desg']
print(data2)
#op:{'id': 22134, 'name': 'Harish', 'salary': 50000}



del data1['id']
print(data1)
#op:{'name': 'Rakesh', 'desg': 'Python Trainee'}


data1['id']=22222
data1['salary']=15000
print(data1)
##op:{'name': 'Rakesh', 'desg': 'Python Trainee'}
##{'name': 'Rakesh', 'desg': 'Python Trainee', 'id': 22222, 'salary': 15000}

print(len(data1))

data3=str(data1) 
print(data1)
print(type(data3))

#METHODS:


print(data1.keys())
print(data2.values())
print(data1.items())
data={'id':22222,'name':"Rakesh",'desg':"Developer"}
data4={'company':"Ojas"}
data.update(data4)
print(data4)

dt={1:'nag',2:'shub',3:'rak'}
dt1={4:'gow'}
dt1.update(dt)
print(dt1)

print(data1.clear())
print(data1)





#Sequence:
seque={"id","name","email"}
data={}
data=data.fromkeys(seque)
print(data)
data=data.fromkeys(seque,23)
print(data)




dat={'id':22222,'name':"Rakesh",'desg':"Developer"}
data=dat.copy()
print(data)


##op:4
##{'name': 'Rakesh', 'desg': 'Python Trainee', 'id': 22222, 'salary': 15000}
##<class 'str'>
##dict_keys(['name', 'desg', 'id', 'salary'])
##dict_values([22134, 'Harish', 50000])
##dict_items([('name', 'Rakesh'), ('desg', 'Python Trainee'), ('id', 22222), ('salary', 15000)])
##{'company': 'Ojas'}
##{4: 'gow', 1: 'nag', 2: 'shub', 3: 'rak'}
##None
##{}
##{'id': None, 'name': None, 'email': None}
##{'id': 23, 'name': 23, 'email': 23}
##{'id': 22222, 'name': 'Rakesh', 'desg': 'Developer'}
'''
'''
dct={1:"arelli",2:"rakesh",3:"srs"}
print(dct.key(2))
OP:Traceback (most recent call last):
  File "C:/Users/ra22222/AppData/Local/Programs/Python/Python39/dictionary_practice.py", line 114, in <module>
    print(dct.key(2))
AttributeError: 'dict' object has no attribute 'key'
'''
dct={1:"arelli",2:"rakesh",3:"srs"}
print(dct.get(3))
print(dct.get(46))

OP:srs
None



