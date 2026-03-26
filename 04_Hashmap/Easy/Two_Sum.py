class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 3rd Solution --> USING Hashmap(Dictionary) --> time complexity: O(n)
        my_lst = []
        my_dict = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in my_dict:
                my_lst.append(i)
                my_lst.append(my_dict[complement])
                return my_lst
            my_dict[nums[i]] = i
        
        # The "Complement" Concept
        # For every number you encounter (let's call it x), you aren't 
        # actually looking for "any" number. You are looking for one specific number: 
        # The Complement --> complement = target - x
        # If the target is 10 and your current number is 7, you are specifically hunting for a 3.

        # The Step-by-Step Logic
        # As you iterate through the array:
            #1) Calculate the Complement: Subtract the current number from the target.
            #2) Check the Dictionary: Ask the dictionary: "Have I seen this complement before?"
                #IF YES: You found the pair! You have the current index, 
                # and the dictionary gives you the complement's index. Done.

                # IF NO: This number hasn't found its partner yet. Store the current 
                # number and its index in the dictionary so a future number can find it.

####################################################################

        # 2nd Solution --> time complexity: O(n squared)
        #--------------
        # my_lst = []
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if j == i:
        #             continue        # In order not to sum the element and itself
        #         if nums[i] + nums[j] == target:
        #             my_lst.append(i)
        #             my_lst.append(j)
        #             return my_lst

####################################################################
        
        # 1st Solution
        #--------------
        # counter1 = -1
        # counter2 = -1
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if j == i:
        #             continue
        #         if nums[i] + nums[j] == target:
        #             counter1 = i
        #             counter2 = j
        #             break
        #     if counter1 != -1:
        #         break
        
        # if counter1 == -1 and counter2 == -1:
        #     return None
        # else:
        #     return [counter1, counter2]
        
