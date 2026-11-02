class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #Binary search the matrix
        start, end = 0 , len(matrix)-1

        while start <= end:
            middle = start + (end- start) // 2
            if matrix[middle][0] > target:
                end = middle - 1
            elif matrix[middle][-1] < target:
                start = middle + 1 
            else:
                break

        if start > end:
            return False 


        #Second Binary Search on the specific row
        l, r = 0 , len(matrix[middle])- 1

        while l <= r:
            m = l + (r-l) // 2
            if matrix[middle][m] > target:
                r = m - 1
            elif matrix[middle][m] < target:
                l = m + 1
            else: 
                return True

        return False #No Target found :{


        













