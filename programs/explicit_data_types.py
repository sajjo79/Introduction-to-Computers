x=str("helloworld")
print(type(x))
print(x)

x=str(54678)
print(type(x),x)

x=int(50)
print(type(x))
print(x)

x=float(5.67)
print(type(x))
print(x)

x=complex(3+6j)
print(type(x))
print(x)

x = list(("apple", "banana", "cherry"))
print(type(x))
print(x)

x = tuple(("apple", "banana", "cherry"))
print(type(x))
print(x)

x = range(6)
print(type(x))
print(x)

x = dict([("name","Ali"),("age" , 36)])
print(type(x))
print(x)

x = set(("apple", "banana", "cherry"))
print(type(x))
print(x)

x = frozenset(("apple", "banana", "cherry"))
print(type(x))
print(x)

x = bool(5)
print(type(x))
print(x)

x = bytes(55)
print(type(x))
print(x)

x = bytearray(5)
print(type(x))
print(x)

x = memoryview(bytes(5))
print(type(x))
print(x)


