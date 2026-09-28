class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = []
        for char in s:
            if char.isalnum():
                cleaned.append(char.lower())
            
        cleaned_string = ''.join(cleaned)

        cleaned_string_length = len(cleaned_string)
        for i in range(cleaned_string_length):
            if cleaned_string[i] != cleaned_string[cleaned_string_length-i-1]:
                return False
        return True