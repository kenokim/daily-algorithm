class Solution:

    def swap(self, nums: List[int], i, j):
        target = nums[j]
        nums[j] = nums[i]
        nums[i] = target


    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 0
        while j < len(nums) - 1:
            j += 1
            if nums[j - 1] != nums[j]:
                i += 1
                self.swap(nums, i, j)

        print(nums[:i+1])

        return i