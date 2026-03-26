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

#------------------------------------------------------------------------------------------------
        
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
        
#------------------------------------------------------------------------------------------------

        # How could I remove duplicates from an array ?

        # 1. The "Set" Method (Fastest & Easiest)
        # This is the standard way. A set in Python is a collection that, by definition, 
          # cannot contain duplicate values.
        
        # Pros: Extremely fast ($O(n)$ time complexity)
        # Cons: It does not preserve the order of the original list.

        # Example
            # nums = [1, 2, 2, 3, 4, 4, 5]
            # unique_nums = list(set(nums))
            # # Result: [1, 2, 3, 4, 5] (but the order might change)
        
        # If you are using Python 3.7+, dictionaries maintain the order in which keys are inserted. 
        # This is the "modern" way to get unique values while keeping the list in its original sequence.

        # Pros: Preserves order and is very fast.
        # Cons: Slightly more memory usage than a set.

        # Example
            # nums = [5, 1, 2, 2, 5, 3]
            # unique_nums = list(dict.fromkeys(nums))
            # # Result: [5, 1, 2, 3]
        
        # 3. The "List Comprehension" Method (Manual Logic)
        # If you want to understand the logic behind it, you can iterate through the list and only add 
          # an element to a new list if it isn't already there.
        
        # Pros: Easy to understand; works in any language.
        # Cons: Very slow (O(n^2) complexity) because for every item, Python has to search the entire new list.

        # Example
            # # nums = [1, 2, 2, 3]
            # unique_nums = []
            # [unique_nums.append(x) for x in nums if x not in unique_nums]
        
        # 4. The "Sorting" Method (Best for Two-Pointer Problems)
        # Since we were just discussing the 3Sum problem, this is how you handle duplicates in a sorted 
          # array without using extra memory (In-place).
        
        # Logic: If the current number is the same as the previous number, skip it.
        
        # Example
            # nums = [1, 1, 2, 2, 3] # Array MUST be sorted
            # unique_nums = []
            # for i in range(len(nums)):
            #     if i > 0 and nums[i] == nums[i-1]:
            #         continue
            # unique_nums.append(nums[i])
