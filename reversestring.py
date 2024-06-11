st =str(input("Enter a string: "))
reversedString = ""
for index in range(len(st)-1, -1, -1):
    reversedString = reversedString+st[index]
print("Reversed String: ", reversedString)
    