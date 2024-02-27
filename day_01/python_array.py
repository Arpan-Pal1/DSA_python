# 25.02.2024 (Array) -> Limited type acceptance

from array import *

a1 = array('i', [5,10,8])

print(type(a1))

for i in a1:
    print(i, end=' - ')

a1.append(100)
print()
for i in a1:
    print(i, end=' - ')


a1.remove(100)
print(a1)
