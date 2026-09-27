from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lettersInWordS = defaultdict(int)
        lettersInWordT = defaultdict(int)

        for char in s:
            lettersInWordS[char]+=1
        
        for char in t:
            lettersInWordT[char]+=1
        
        return lettersInWordT==lettersInWordS
        