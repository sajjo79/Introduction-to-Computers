
a=5
fact=1
while(a>1):
    fact=fact*a
    a=a-1
print(fact)
#5*4*3*2=120
"""
#######################################################
count=0
sum=0
while(count<5):
    sum=sum+count;
    count=count+1
    print("the value is", count)
    print("The sum is ",sum)
print("after the while loop body")

count=0
sum=0
while(count<5):
    sum=sum+count;
    count=count+1
    print("the value is", count)
    break
    print("The sum is ",sum)
print("after the while loop body")
#######################################################
count=0
sum=0
while(True):
    a=input("Please enter a number::")
    a=int(a)
    if(a<0):
        break
    print("You have entered the value:",a)
print("after the while loop body")


#######################################################
count=0
sum=0
while(count<5):
    sum=sum+count;
    count=count+1
    print("the value is", count)
    print("The sum is ",sum)
print("after the while loop body")

count=0
sum=0
while(count<5):
    sum=sum+count;
    count=count+1
    print("the value is", count)
    continue
    print("The sum is ",sum)
print("after the while loop body")

count=0
sum=0
while(count<5):
    sum=sum+count;
    count=count+1
    print("the value is", count)
    if(count%2==0):
        continue
    print("The sum is ",sum)
print("after the while loop body")
"""