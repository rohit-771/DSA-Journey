class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        if m * n != r * c:
            return mat

        result = []
        temp = []

        for row in mat:
            for value in row:
                temp.append(value)

        index = 0

        for i in range(r):
            row = []
            for j in range(c):
                row.append(temp[index])
                index += 1
            result.append(row)

        return result
        