string = input("Enter a string: ")
# Remove non-alphanumeric characters and convert to lowercase
sentence = ''.join(filter(str.isalnum, string)).lower()

# Check if the cleaned sentence is equal to its reverse
if sentence == sentence[::-1]:
    print(f'"{string}" is a palindrome.')
else:
    print(f'"{string}" is not a palindrome.')
