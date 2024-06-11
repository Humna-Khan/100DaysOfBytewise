string = input("Enter a string: ")
reversed_string = string[::-1]

if reversed_string == string:
    print(string," is palindrome.")
    
else:
    print(string, " is not palindrome.")
