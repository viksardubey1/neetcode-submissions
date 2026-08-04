class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        first_ind = [line[0] for line in matrix]
        working_list = []
        l, r = 0, len(first_ind) - 1
        while l <= r:
            mid = (l + r) // 2
            if mid == len(first_ind) - 1 or (target >= first_ind[mid] and target < first_ind[mid + 1]):
                working_list = matrix[mid]
                break
            elif target < first_ind[mid]:
                r = mid - 1
            else:
                l = mid + 1
        lo, hi = 0, len(working_list) - 1
        while lo <= hi:
            mid = (hi + lo) // 2
            if target == working_list[mid]:
                return True
            elif target < working_list[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        return False