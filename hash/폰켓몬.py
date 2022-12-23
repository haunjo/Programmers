def solution(nums):
    answer = 0
    n = len(nums)/2
    nums = set(nums)
    answer = n if n < len(nums) else len(nums)
    return answer