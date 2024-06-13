def longestPalindromicss(s):
    if not s:
        return ""

    n = len(s)
    longest = ""

    def lPalindrome(left, right):
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    for i in range(n):
    
        palindrome_odd = lPalindrome(i, i)
        palindrome_even = lPalindrome(i, i + 1)
        
        if len(palindrome_odd) > len(longest):
            longest = palindrome_odd
        if len(palindrome_even) > len(longest):
            longest = palindrome_even
    return longest

if __name__ == "__main__":
    string = input("Enter a string: ")
    palindrome = longestPalindromicss(string)
    print("Longest palindromic substring:", palindrome)
