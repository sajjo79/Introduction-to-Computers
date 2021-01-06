# ========= Simple Loop
a=1
while(a<=5):
    print("#")
    a=a+1
print("five times # is printed")

# ======== Nested Loop
a=1
while(a<=5):
   b = 1
   while(b<=3):
        print("#")
        b=b+1
   a=a+1
print("Fifteen times # is printed")

#========= Tables of 2,3,4,5
a=2
while(a<=5):
    b=1
    while(b<=10):
        print(a,"*",b,"=",a*b)
        b=b+1
    a=a+1
print("tables of 2,3,4,5 printed")

#=== finding the sum of factorial from 1 to 5
num=1
sum=0
while(num<=5):
    fact=1
    b=num
    while(b>=1):
        fact=fact*b
        b=b-1
    print("factorial of ",num,"is",fact)
    sum=sum+fact
    num=num+1
print("sum of factorials",sum)

print("hello",end='')
print("world",end='')
print(" on same line")