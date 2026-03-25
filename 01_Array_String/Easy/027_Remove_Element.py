class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # We used: Two-Pointer technique.
            # i is the "Explorer" pointer
            # write_index is the "Anchor" pointer

        # Second Attempt

        write_index = 0  # This tracks where the next 'good' number goes
        
        for i in range(len(nums)):
            if nums[i] != val:
                # If it's a good number, move it to the front
                nums[write_index] = nums[i]
                write_index += 1
                
        return write_index
        
#---------------------------------------------------
        # My First Attempt ---> Not Correct
        #------------------
        # no_of_elements = len(nums)
        # for i in range(len(nums)):
        #     if nums[i] == val:
        #         no_of_elements -= 1
        #         nums[i] = '_'

        # Why there is a problem in that solution ?!
        # Because ---> you change [3, 2, 2, 3] to ['_', 2, 2, '_']
        
