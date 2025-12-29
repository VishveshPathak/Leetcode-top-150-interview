class Solution:
    def add_element(self, nums, ins):
        for i in range(len(nums)):          #run through the array until inserted element < nums[i] 
            if nums[i] > ins:
                x = len(nums)-1
                while x>i:                  #start from back of the array and shift all elements right until x = i
                    nums[x] = nums[x-1]
                    x = x-1
                nums[i] = ins
                break
        return nums
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        count = 0
        while count < n:                        #if nums2 is empty, return nums1
            if nums1[m-1]<=nums2[count]:        #if nums2[count] > max element of nums1, increase size on nums1 by 1 and append at that position
                nums1[m] = nums2[count]
            else:                               #else insert at correct position and shift entire array right till the position
                nums1 = self.add_element(nums1, nums2[count])
            m = m+1
            count = count+1

            