"""
This file presents the concept of automatic and explict data type conversion
"""
# automatic type conversion - conversion
a=5
print(type(a),a)

b=5.6
a=b
print(type(a),a)

c=5+6j
a=c
print(type(a),a)

# explicit type conversion - casting

a=5
print(type(a),a)

b=float(a)
print(type(b),b)

c=complex(a)
print(type(c),c)

d=str(a)
print(type(d),d)