class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)

        zeros = 0

        for x in arr:
            if x == 0:
                zeros += 1

        i = n - 1
        j = n + zeros - 1

        while i < j:

            if j < n:
                arr[j] = arr[i]

            j -= 1

            if arr[i] == 0:
                if j < n:
                    arr[j] = 0
                j -= 1

            i -= 1
        