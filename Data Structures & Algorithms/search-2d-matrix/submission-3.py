class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix[0])
        n = len(matrix)
        l, r = 0, n-1
        while l <= r:
            mid = (r + l)//2
            if matrix[mid][0] <= target <= matrix[mid][m-1]:
                l1, r1 = 0, m-1
                while l1 <= r1:
                    mid1 = (r1 + l1)//2
                    if matrix[mid][mid1] == target:
                        return True
                    elif matrix[mid][mid1] < target:
                        l1 = mid1 + 1
                    else:
                        r1 = mid1 - 1
                return False
            elif matrix[mid][0] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False
            


