class Solution:
    
    # Function to search a given number in strictly sorted matrix.
    def searchMatrix(self, mat, x):
        n = len(mat)
        m = len(mat[0])
        
        low = 0
        high = n * m - 1
        
        # Binary search ek 1D array ki tarah kar rahe hain matrix par
        while low <= high:
            mid = (low + high) // 2
            
            # Mid ko 2D index mein convert kar rahe hain
            row = mid // m
            col = mid % m
            
            if mat[row][col] == x:
                return True  # Element mil gaya
            elif mat[row][col] < x:
                low = mid + 1  # Right half mein jao
            else:
                high = mid - 1  # Left half mein jao
        
        return False  # Element nahi mila
