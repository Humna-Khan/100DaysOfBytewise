def factorilofnumber(num):
    if num==0:
        return 1
    else:
        return num * factorilofnumber(num-1)
    
num = int(input("Enter a number to find its factorial: "))
print("The factorial of ", num, " is ",factorilofnumber(num))
    