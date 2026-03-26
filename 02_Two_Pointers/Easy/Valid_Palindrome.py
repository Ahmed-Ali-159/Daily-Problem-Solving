class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lower_s = s.lower()             # lower all characters
        
        # Keep the character 'c' ONLY if it is alphanumeric
        clean_s = "".join(c for c in lower_s if c.isalnum())

        first = 0
        last = len(clean_s) - 1
        while first < last:
            if clean_s[first] != clean_s[last]:
                return False
            first += 1
            last -= 1
        return True
        
        
        
