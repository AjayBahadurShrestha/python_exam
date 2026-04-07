l=[10,20,30,40,50]
l.extend([1,2,3])
print(f'updated list : {l}')
l.extend(range(1,10))
print(f'updated list : {l}')


l.extend('Kathmandu')
print(f'updated list : {l}')

# l.remove('Kathmandu')
# print(f'updated list : {l}') Error!!!!!!!!!!!!1

l.remove(50)
print(f'updated list : {l}')

# l.remove(500)
# print(f'updated list : {l}') ERROr!!!!!!!!!!!!!

l.pop()
print(f'updated list : {l}')

l.reverse()
print(f'updated list : {l}')


