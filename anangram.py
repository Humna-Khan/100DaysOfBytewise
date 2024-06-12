
string1 = input("Enter the first word: ")
string2 = input("Enter the second word: ")

str1 = ''.join(string1.lower().split())
str2 = ''.join(string2.lower().split())

if sorted(str1) == sorted(str2):
    print(f'"{string1}" and "{string2}" are anagrams.')
else:
    print(f'"{string1}" and "{string2}" are not anagrams.')
