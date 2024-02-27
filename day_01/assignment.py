# Array

'''
1. Given an array with some int type values. WAP to sort array values 


import array as ar

a1 = ar.array('i', [5,100,2, 100, 185,50,6])

for i in range(len(a1)):
    j = i + 1
    while j < len(a1):
        if a1[j] < a1[i]:
            a1[i], a1[j] = a1[j], a1[i]
        j+=1

print(a1)
'''


# List 
"""
Remove all the non-int value from the list

💡 tips: For historic reasons, Python treats bool as a subclass of int. This means that True is an instance of int.
    Originally, Python didn’t have a separate bool type. Instead, truth values were represented as 1 (for True) and 0 (for False).
    When bool was introduced, it needed to be compatible with existing code. So, True and False were designed to behave like 1 and 0, respectively, for backward compatibility.
    As a result, True inherits f tips: 


li = ['Arpan', 1, True, 0+5j, 15]
filtered_list = [x for x in li if isinstance(x, int) and not isinstance(x, bool)]
print(filtered_list)

print(li)

"""

"""AVG of elements of a list


li = [100,10]

total = 0
for i in li:
    total = total + i
    avg = total/len(li)

print(avg)

"""

""" First N prime number

n = int(input("enter the range "))

prime_number = []

for i in range(2, n+1):
    count = 0
    for j in range(2, i//2 + 1):
        if i%j==0:
            count += 1
    if count == 0:
        prime_number.append(i)   

print(prime_number)

"""


"""N term fibonacci series"""

n = int(input("enter the range "))

fibo = [0,1]
first = 0
second = 1
for i in range(2, n):
    first, second = second, second + first
    fibo.append(second)
print(fibo)