class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""
        for i in s:
            new_str += i.lower() if i.isalnum() else ""
        
        return True if new_str == new_str[::-1] else False