class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        # 1st Solution ---> Does not count because I made a new list --> I should solve it in-place
        
        # Handle special case -->  The k > length Trap
        if len(nums) < k:
            k = k % len(nums)

        my_lst = []
        index = len(nums) - k   
        while index < len(nums):
            my_lst.append(nums[index])
            index += 1
        for j in range(len(nums) - k):
            my_lst.append(nums[j])
        
        nums[:] = my_lst       # Here I COPIED the values of my_lst to nums
        return nums

# The k > length Trap
# Why this: k = k % len(nums)

# What happens if the array has 3 elements but k = 10? 
# Rotating a 3-element array 3 times brings it back to the start. 
# Rotating it 10 times is the same as rotating it 1 time (10 mod 3 = 1).

# Without a modulo operator, your index = len(nums) - k will result in 
# a negative index or an out-of-bounds error.

        
