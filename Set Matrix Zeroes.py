class Solution:
    def setMatrixZeroes(self, mat):
        n = len(mat)
        m = len(mat[0])
        
        # Pehle check karo agar first row ya first column mein zero hai ya nahi
        first_row_has_zero = any(mat[0][j] == 0 for j in range(m))
        first_col_has_zero = any(mat[i][0] == 0 for i in range(n))

        # Baaki matrix ko traverse karo aur agar koi element 0 mila
        # toh uske row aur column ke first cell ko 0 mark kar do
        for i in range(1, n):
            for j in range(1, m):
                if mat[i][j] == 0:
                    mat[i][0] = 0
                    mat[0][j] = 0

        # Marked cells ki madad se baaki matrix ko update karo
        for i in range(1, n):
            for j in range(1, m):
                if mat[i][0] == 0 or mat[0][j] == 0:
                    mat[i][j] = 0

        # Agar first row mein zero tha toh poori row ko zero kar do
        if first_row_has_zero:
            for j in range(m):
                mat[0][j] = 0

        # Agar first column mein zero tha toh poora column zero kar do
        if first_col_has_zero:
            for i in range(n):
                mat[i][0] = 0

        return mat
