class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        maxi=sum(reward2)

        diff = []
        for i in range(len(reward1)):
            diff.append(reward1[i]-reward2[i])
        
        diff.sort(reverse=True)
        for i in range(k):
            maxi+=diff[i]
        return maxi
        