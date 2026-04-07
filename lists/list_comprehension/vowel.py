l=['India','Nepal','Australai','England','Norway','Pakistan','USA']
v=['A','E','I','O',"U"]
l3=[x for x in l if x[0] in v]
l4=[x for x in l if x[0] not in v]

print(l3)

print(l4)


l5=[(x,len(x)) for x in l ]
print(l5)

l6=[{x:len(x)} for x in l ]
print(l6)
