a=10
b=20
print(a<15 and b<30)
print(a<15 or b<20)
print(not(a<10))

# complex expression
print((a<10 and b<30) or (a<20 and b<40))
print((a<10 or b<30) and (a<20 or b<40))
print((a<10 or b<30) or (a<20 and b<40))
print((a<10 and b<30) or (a<20 or b<40))
print((a<10 and b<30) and (a<20 and b<40))
