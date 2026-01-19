class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        n = []
        T = True
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):

                if nums[i] + nums[j] != target:
                    T = False
                else:
                    n = [i, j]
                    T = True
                    
                    break #this is for j loop

            if T == True:
                return n

                break  # this is for i loop


                