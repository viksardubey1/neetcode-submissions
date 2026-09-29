class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_lo, row_hi = 0, len(matrix) - 1
        row = 0
        while row_hi >= row_lo:
            row_mid = (row_hi + row_lo) // 2
            if target >= matrix[row_mid][0]:
                row_lo = row_mid + 1
            else:
                row_hi = row_mid - 1
        if row_hi < 0:
            return False

        new_row = matrix[row_hi]
        lo, hi = 0, len(new_row) - 1
        while hi >= lo:
            mid = (hi + lo) // 2
            if new_row[mid] == target:
                return True
            elif new_row[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1

        return False





        