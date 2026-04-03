class Solution:
    def isPalindrome(self, s: str) -> bool:
        extracted_string =  "".join([c for c in s if c.isascii() and c.isalnum()])
        if s == "":
            return False
        
        first = 0
        last = len(extracted_string)-1

        while  first < last:
            if extracted_string[first].lower()!=extracted_string[last].lower():
                return False
            first+=1
            last-=1
        return True