n = int(input("Enter the number of terms for the fibonacci series: "))
firstNumber = 0
secondNumber = 1
for index in range(n):
    print(firstNumber, end=" ")
    nextNumber = firstNumber + secondNumber
    firstNumber = secondNumber
    secondNumber = nextNumber