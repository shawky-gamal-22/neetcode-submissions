class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_text = "".join(char.lower() for char in s if char.isalnum())
        

        st= 0 
        ed= len(cleaned_text) - 1

        while st <= ed:
            if cleaned_text[st] != cleaned_text[ed]:
                return False
            
            st += 1
            ed -= 1
        return True