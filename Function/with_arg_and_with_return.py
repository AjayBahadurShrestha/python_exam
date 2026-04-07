def vote(name,age):
  if age>=18 : 
    return True
  else:
    return False

status=vote("ajay",18)
if status:
    print(f"is eligible for vote")
else:
  print(f"isnot eligible for vote")

