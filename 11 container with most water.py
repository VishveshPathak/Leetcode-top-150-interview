"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.
"""
#solution:

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxleft = 0
        i = 0
        j = len(height) - 1
        maxright = j
        maxarea = abs(j-i)*min(height[j], height[i])
        while i<j:
            if maxarea<(min(height[i], height[j])*abs(j-i)):
                maxarea = min(height[i], height[j])*abs(j-i)
            if height[i]<height[j]:
                i = i + 1
            else:
                j = j - 1
        return maxarea
        