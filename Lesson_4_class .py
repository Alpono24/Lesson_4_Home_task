# 111
"""a = 5
b = 10
lst = [1, 2, 'aw']
print(type(a), dir(a))
print(type(b), dir(b))
print(type(lst), dir(lst))"""

# 222
"""import sys
lst = [1, 2, 'awd']
print(sys.getrefcount(lst))"""

# 333
"""from sys import intern
str1 = "qwqwqwqw"*100000
str2 = "qwqwqwqw"*100000
print(id(str1))
print(id(str2))
str11 = intern(str1)
str22 = intern(str2)
print(id(str11))
print(id(str22))"""

# 444
"""int_a=20
int_b=20
print(id(int_a))
print(id(int_b))
"""

# 555
import sys

a = 9109
b = 9109
c = [a, b]
print(sys.getrefcount(a))
"""del b
del c"""
print(sys.getrefcount(a))

# 666
import sys
a=[]
b=[a]
a.append(b)
print(sys.getrefcount(a))
print(a)
