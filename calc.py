num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number number: "))
op = input("Enter an operator(+,-,*,/): ")
if op == "+":
    print("The sum of the two number is ", num1+num2)
elif op == "-":
    print("The difference of the two numbers is ", num1-num2)
elif op =="*":
    print("The product of the two numbers is ", num1*num2)
elif op == "/":
    print("The two numbers when divided gives ", num1/num2)
else:
    print("You have entered an invalid operator.\nTry again!")