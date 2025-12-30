#solution: 
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        limit = math.floor(len(nums)/2)     #set limit as floor of n/2
        current = nums[0]
        maxval = 1000000001                 #upper limit of input
        for i in range(len(nums)):          #iterate through all nums once
            count = 0
            current = nums[i]
            if nums[i]!=maxval:
                for j in range(len(nums)):  #set all numbers that are same as nums[i] as upperlimit
                    if current == nums[j]:   
                        count = count + 1
                        if count>limit:     #check count exceeds limit, then return
                            return current
                        nums[j] = maxval

#O(n) time and O(1) space best attempt:

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        x = 0
        ignore = 1000000001
        direction = 0
        counter = 0
        checking = nums[0]
        checkingcount = 0
        limit = math.floor(len(nums)/2)
        i=0
        while i<len(nums):                              #iterate through the array in forward direction
            print(i, checking, checkingcount, counter)
            print(nums)
            if i == len(nums)-1:
                if nums[i] == checking:                 #check if last number is matching, and count exceeds limit, then return
                    checkingcount = checkingcount + 1
                    nums[i] = ignore
                    if checkingcount > limit:
                        return checking
                i=0                                     #reset loop if inputs still pending
                if checkingcount > 0:
                    checkingcount = 0
                    while nums[counter] == ignore:      #find the next number in nums which is not upper limit of input
                        counter = counter + 1
                    checking = nums[counter]
            else:
                if nums[i] == checking:                 #if found number, set other numbers as upper limit and focus on counting current checking.
                    nums[i] = ignore
                    checkingcount = checkingcount + 1
                    if checkingcount > limit:           #exit if condition met
                        return checking
            i = i+1
            
            
            
                
            
            
                