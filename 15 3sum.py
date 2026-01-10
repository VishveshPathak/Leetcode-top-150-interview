"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
"""
#solution:
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        P = []
        N = []
        Z = []
        sol = set()
        for i in nums:
            if i<0:
                N.append(i)
            elif i == 0:
                Z.append(i)
            else:
                P.append(i)
        
        p = set(P)
        n = set(N)
        z = set(Z)
        
        if len(Z)>=3:
            sol.add((0, 0, 0))
        for i in P:
            if i*-1 in n:
                if len(Z)>0:
                    sol.add((-1*i, 0 ,i))
        
        for i in range(len(P)):
            for j in range(i+1, len(P)):
                if i!=j:
                    if -1*(P[i]+P[j]) in n:
                        key = sorted([-1*(P[i]+P[j]), P[i], P[j]])
                        sol.add(tuple(key))
        for i in range(len(N)):
            for j in range(i+1, len(N)):
                if i!=j:
                    if -1*(N[i]+N[j]) in p:
                        key = sorted([-1*(N[i]+N[j]), N[i], N[j]])
                        sol.add(tuple(key))
        sol1 = []
        for i in sol:
            sol1.append([i[0], i[1], i[2]])
        return sol1