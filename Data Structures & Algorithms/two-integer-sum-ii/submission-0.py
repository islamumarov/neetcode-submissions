class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first = 0
        second = len(numbers)-1

        while first < second:
            cur_sum = numbers[first] + numbers[second]
            if cur_sum > target:
                second -=1
            elif cur_sum < target:
                first += 1
            else:
                return [first+1, second+1]
        
        return [-1,-1]