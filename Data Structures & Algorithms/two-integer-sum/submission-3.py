class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_numbers = dict()

        for i, num in enumerate(nums):
            needed_number = target - num
            #we don't want the two numbers to be the same
            if needed_number in seen_numbers:
                return [seen_numbers[needed_number], i]
            seen_numbers[num]=i