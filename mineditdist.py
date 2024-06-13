def minEditDist(word1, word2):
    dic = {}
    
    def calc(i, j):
        if i == 0:
            return j  
        if j == 0:
            return i  
        
        if (i, j) in dic:
            return dic[(i, j)]
        
        if word1[i - 1] == word2[j - 1]:
            result = calc(i - 1, j - 1)
        else:
            result = 1 + min(calc(i - 1, j),  
                            calc(i, j - 1), 
                            calc(i - 1, j - 1)) 
        
        dic[(i, j)] = result
        return result
    
    return calc(len(firstWord), len(seocdWord))

firstWord = "kitten"
seocdWord = "sitting"
result = minEditDist(firstWord, seocdWord)
print(f"The minimum edit distance between '{firstWord}' and '{seocdWord}' is: {result}")
