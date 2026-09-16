class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 1, len(numbers)
        while numbers[left - 1] + numbers[right - 1] != target:
            if numbers[left - 1] + numbers[right - 1] < target:
                left += 1
            else:
                right -= 1
        return [left, right]


