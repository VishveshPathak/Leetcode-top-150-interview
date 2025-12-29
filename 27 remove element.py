#Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
#Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
#Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
#Return k.

#solution:
class Solution:
    def shift_array(self, nums, ind):   #function to shift array by 1 each time a new element is found
        x = ind
        while x<len(nums)-1:            #shift the array left from index position to end
            nums[x] = nums[x+1]
            x = x+1
        nums[len(nums)-1] = -1          #replace end variable with -1(out of range)
        return nums
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)-1, -1, -1):        #iterate backwards and find all matching values
            if nums[i] == val:
                nums = self.shift_array(nums, i)    #call the function to remove from backward
                print(nums)
                k = k+1                             #count modifications

        return len(nums)-k                          #return unmodified elements