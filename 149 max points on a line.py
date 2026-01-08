"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.
Example 1:
Input: points = [[1,1],[2,2],[3,3]]
Output: 3
"""
#solution:
class Solution:
    def addSlopes(self, x1, y1, x2, y2, hashmap):
        if x2-x1 == 0:
            m = 'inf'
            c = x2
        else:
            m = (y2-y1)/(x2-x1)
            c = y2-(m*x2)
        string = str(m)+', '+str(c)
        if string in hashmap:
            if [x1, y1] not in hashmap[string]:
                hashmap[string].append([x1, y1])
            if [x2, y2] not in hashmap[string]:
                hashmap[string].append([x2, y2])
        else:
            hashmap[string] = []
            hashmap[string].append([x1, y1])
            if [x2, y2] not in hashmap[string]:
                hashmap[string].append([x2, y2])
        return hashmap

    def maxPoints(self, points: List[List[int]]) -> int:
        hm = {}
        if len(points) == 1:
            return 1
        for i in range(len(points)):
            for j in range(len(points)):
                if i!=j:
                    hm = self.addSlopes(points[i][0], points[i][1], points[j][0], points[j][1], hm)
        Max = 0
        for i in hm:
            if len(hm[i])>Max:
                Max = len(hm[i])
        return Max