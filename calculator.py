def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    if(n2==0):
        return "invalid divission"
    else:
        return n1/n2
def square(n1):
    return n1**2
def power(n1,n2):
    return n1**n2

n1=int(input("Enter 1st number: "))
n2=int(input("Enter 2nd number: "))
opp=input("Enter operation: ")
if(opp == "add"):
    res=add(n1,n2)
elif(opp == "sub"):
    res=sub(n1,n2)
elif(opp=="mul"):
    res=mul(n1,n2)
elif(opp=="div"):
    res=div(n1,n2)
elif(opp=="square"):
    res=square(n1)
elif(opp=="power"):
    res=power(n1,n2)
else:
    print("invalid")
print("Result:", res)
