def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    if(n2==0):
        return "invalid division"
    else:
        return n1/n2
def square(n1):
    return n1**2
def power(n1,n2):
    return n1**n2

if __name__ == "__main__":
    num1=int(input("ENter first number:"))
    num2=int(input("Enter second number:"))
    print("Addition:", add(num1, num2))
    print("Subtraction:", sub(num1, num2))
    print("Multiplication:", mul(num1, num2))
    print("Division:", div(num1, num2))
    print("Square of first number:", square(num1))
    print("Power:", power(num1, num2))
