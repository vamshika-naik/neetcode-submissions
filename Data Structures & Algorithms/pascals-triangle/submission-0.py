class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = [[] for _ in range(numRows)]
        pascal[0].append(1)

        for i in range(1, numRows):
            pascal[i] = [1] * (i+1)
            for j in range(1, i):
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]

        return pascal