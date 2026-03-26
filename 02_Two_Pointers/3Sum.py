class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # This solution is not correct because you don't solve the problem of: 
                # the solution set must not contain duplicate triplets

        triplets = []
        sorted_nums = sorted(nums)
        for i in range(len(sorted_nums)):
            if sorted_nums[i] > 0:     # There will be no triplets that sum to 0
                break
            j = i + 1                   # left pointer
            k = len(sorted_nums) - 1    # right pointer
            while j < k:
                if sorted_nums[j] + sorted_nums[k] < - sorted_nums[i]:  # So we need move the left pointer forward
                    j += 1
                elif sorted_nums[j] + sorted_nums[k] > - sorted_nums[i]:  # So we need move the right pointer backward
                    k -= 1
                elif sorted_nums[j] + sorted_nums[k] == - sorted_nums[i]:
                    triplets.append([sorted_nums[i], sorted_nums[j], sorted_nums[k]])
                    j += 1
                    k -= 1
        
        unique_triplets = [list(t) for t in set(tuple(x) for x in triplets)]
        return unique_triplets

        
        # Example of Removing duplicates from an Array of arrays
        
        # When you move from a simple list of numbers to an array of arrays (a 2D list), things get a bit trickier.
        # Python's set() method, which we used before, will actually throw a TypeError: unhashable type: 'list' because
        # lists are "mutable" (they can be changed), and sets only accept "immutable" items.

        # triplets = [[-1, 0, 1], [-1, -1, 2], [-1, 0, 1]]

        # # 1. Convert inner lists to tuples
        # # 2. Put them in a set to kill duplicates
        # # 3. Convert back to a list of lists
        # unique_triplets = [list(t) for t in set(tuple(x) for x in triplets)]

        # # Result: [[-1, 0, 1], [-1, -1, 2]]        
        
