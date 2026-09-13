class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        greater = {}

        for num in nums2:
            while stack and num > stack[-1]:
                smaller = stack.pop()
                greater[smaller] = num

            stack.append(num)

        for num in stack:
            greater[num] = -1

        ans = []

        for num in nums1:
            ans.append(greater[num])

        return ans
        
        