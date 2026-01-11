"""
You are given a sorted unique integer array nums.
A range [a,b] is the set of all integers from a to b (inclusive).
Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.
Each range [a,b] in the list should be output as:
    "a->b" if a != b
    "a" if a == b
Example 1:
Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
"""
#solution:
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        sol = []
        soltemp = ""
        count = 0
        if len(nums)==0:
            return nums
        elif len(nums) == 1:
            return [str(nums[0])]
        for i in range(len(nums)-1):
            if count == 0:
                soltemp = soltemp+str(nums[i])
                count = count + 1
                if nums[i]!=nums[i+1]-1:
                    sol.append(soltemp)
                    soltemp = ""+str(nums[i+1])
                    count = 1
                else:
                    count = count + 1

            else:
                if nums[i] == nums[i+1] - 1:
                    count = count + 1
                else:
                    if count>1:
                        soltemp = soltemp+'->'+str(nums[i])
                        sol.append(soltemp)
                        count = 1
                        soltemp = ""+str(nums[i+1])
                    else:
                        sol.append(soltemp)
                        soltemp = ""+str(nums[i+1])
                        count = 1
            print(soltemp, count, i)
        if count == 1:
            sol.append(soltemp)
        else:
            soltemp = soltemp + '->'+str(nums[-1])
            sol.append(soltemp)
        print(sol)
        return sol