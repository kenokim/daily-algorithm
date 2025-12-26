class Solution:
    def find_jk(self, nums: List[int], nums_i, i):
        j, k = 0, len(nums)-1
        jk_list = []

        while j < k:
            sum_ = nums[j] + nums[k]

            if nums_i == -sum_:
                if j != i and k != i:
                    jk_list.append([nums[j], nums[k]])
                    
                k -= 1
                j += 1
            
            elif nums_i > -sum_:
                k -= 1
            
            else:
                j += 1

        return jk_list

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answers = []
        nums.sort()
        for i in range(len(nums)):
            jk_list = self.find_jk(nums, nums[i], i)
            if jk_list:
                for jk in jk_list:
                    sums_ = [nums[i]] + jk
                    sums_.sort()
                    if sums_ not in answers:
                        answers.append(sums_)
        
        return answers
        

# nums[i] = -nums[j] - nums[k]
# [-4, -1, -1, 0, 1, 2]
# O(N^2) + O(NlgN)

"""
2-sum algorithm:
  1. hashmap O(N)
  2. sort + 2-pointers O(N) + O(NlgN)

3-sum 은 1, 2 둘 다 O(N^2) 이다.

if - elif - else 

"""