class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        #This is my first solution --> and I made another solution

        # new_s = s.strip()
        # lst = []
        # word = ""
        # for i in range(len(new_s)):
        #     if (new_s[i] == " ") or ():
        #         lst.append(word)
        #         word = ""
        #     elif i < len(new_s) - 1:
        #         word += new_s[i]
        #     else:                   #To handle the last character
        #         word += new_s[i]
        #         lst.append(word)

        # return len(lst[-1])

#---------------------------------------------------------------------

# Another Solution:
        new_s = s.strip()
        count = 0
        for i in range(len(new_s) - 1, -1, -1):
            if new_s[i] == " ":
                break
            count += 1
        return count

#--------------------------------------------------------------------

#The idea of the second solution is this:

# The "Boyer-Moore" Efficient Solution (No List)
# In a coding interview, the "gold standard" for this problem is to work backwards. 
# If you only need the last word, why build a list of all the words?
    # 1) Strip the trailing spaces.
    # 2) Start at the end of the string.
    # 3) Count until you hit a space or the beginning of the string.
        
        
