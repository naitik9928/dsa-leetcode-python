class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row=len(matrix)
        col=len(matrix[0])
        for i in range(row-1):
            for j in range(i+1,row):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

        for k in range(row):
            matrix[k].reverse()