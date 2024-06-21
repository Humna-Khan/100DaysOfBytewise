def lcsubsequence(s1, s2):
    len1 = len(s1)
    len2 = len(s2)
    
    dynamicProg = [[0] * (len2 + 1) for _ in range(len1 + 1)]
    
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if s1[i - 1] == s2[j - 1]:
                dynamicProg[i][j] = dynamicProg[i - 1][j - 1] + 1
            else:
                dynamicProg[i][j] = max(dynamicProg[i - 1][j], dynamicProg[i][j - 1])
    
    lcsSubsequence = []
    i, j = len1, len2
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            lcsSubsequence.append(s1[i - 1])
            i -= 1
            j -= 1
        elif dynamicProg[i - 1][j] >= dynamicProg[i][j - 1]:
            i -= 1
        else:
            j -= 1
    
    lcsSubsequence.reverse()
    
    return ''.join(lcsSubsequence)

s1 = "AGGTAB"
s2 = "GXTXAYB"
result = lcsubsequence(s1, s2)
print("Longest Common Subsequence (LCS) is:", result)