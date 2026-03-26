class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == "":                 # Just to handle this special case
            return True
        index = 0                   # Here is the pointer of s --> the smaller
        for i in range(len(t)):
            if t[i] == s[index]:    # I will move the pointer of s in case there is a match
                index += 1
                if index == len(s):
                    return True
    
        return False   
         
