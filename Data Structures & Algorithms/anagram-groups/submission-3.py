from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            countOfLetters = [0]*26
            for char in word:
                #we want to keep it within an array of 26 so we aren't wasting space
                countOfLetters[ord(char)-ord('a')]+=1
            #keys for dictionaries need to be immutable so therefore it needs to be a tuple instead of a l
            key = tuple(countOfLetters)
            anagrams[key].append(word)

        return list(anagrams.values())