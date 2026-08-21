class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans=-1
        start=0
        end=len(nums)-1
        while start<=end:
            mid=(start+end)//2
            
            if nums[mid]==target:
                ans=mid
                end=mid-1
            elif nums[mid]<target:
                start=mid+1
            else:
                end=mid-1
        
        ans2=-1
        start=0
        end=len(nums)-1
        while start<=end:
            mid=(start+end)//2
            
            if nums[mid]==target:
                ans2=mid
                start=mid+1
            elif nums[mid]<target:
                start=mid+1
            else:
                end=mid-1
        return [ans, ans2]
        