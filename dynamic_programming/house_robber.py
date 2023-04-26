'''
You are planning to rob houses on a specific street, and you know that every house on the street has a certain amount of money hidden.
The only thing stopping you from robbing all of them in one night is that adjacent houses on the street have a connected security system.
The system will automatically trigger an alarm if two adjacent houses are broken into on the same night.

Given a list of non-negative integers nums representing the amount of money hidden in each house,
determine the maximum amount of money you can rob in one night without triggering an alarm.
'''

from functools import lru_cache
def solution1(nums):
    return house(tuple(nums))

@lru_cache(maxsize=1000)
def house(nums):
    if len(nums) == 0:
        return 0
    return max(house(nums[1:]), house(nums[2:]) + nums[0])

def solution2(nums):
    n = len(nums)
    memo = [0] * (n + 2)
    if n == 2 or n == 1:
        return max(nums)
    if n == 3:
        return max(nums[0] + nums[2], nums[1])
    memo[0] = 0
    memo[1] = 0
    memo[2] = nums[0]
    for i in range(3, n + 2):
        tmp1 = nums[i - 3] + memo[i - 3]
        tmp2 = nums[i - 2] + memo[i - 2]
        memo[i] = max(tmp1, tmp2)
    return max(memo[-1], memo[-2])
def solution2(nums):
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return nums[0]
    elif len(nums) == 2:
        return max(nums)
    sub = []
    prev_2 = nums[0]
    prev_1 = nums[1]
    sub.append(prev_2)
    sub.append(prev_1)
    prev_3 = 0
    for i in nums[2:]:
        if prev_3 < prev_2:
            sub.append(i + prev_2)
        else:
            sub.append(i + prev_3)
        prev_3,prev_2 = prev_2,prev_1
        prev_1 = sub[-1]
    return max(sub)