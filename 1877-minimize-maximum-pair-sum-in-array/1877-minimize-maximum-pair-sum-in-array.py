class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        i=0
        j=n-1
        maxi=0
        while i<j:
            pair = nums[i]+nums[j]
            maxi = max(maxi, pair)
            i+=1
            j-=1
        return maxi

        


        