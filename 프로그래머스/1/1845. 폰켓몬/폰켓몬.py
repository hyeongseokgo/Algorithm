def solution(nums):
    se = len(set(nums))
    if len(nums)/2 > se:
        return se
    else:
        return len(nums)/2