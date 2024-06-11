string = input("Enter a string: ")
count = 0
for index in range(len(string)):
    if string[index].lower() == "a" or string[index].lower() == "e" or string[index].lower() == "i" or string[index].lower() == "o" or string[index].lower() == "u" or string[index].upper() == "A" or string[index].upper() == "E" or string[index].upper() == "I" or string[index].upper() == "O" or string[index].upper() == "U":
        count = count+1
print("The number of vowels is: ", count)
    