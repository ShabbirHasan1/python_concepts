# Given an array, find the contiguous subarray with the largest sum
'''
The runtime complexity of this solution is linear, O(n)
The memory complexity of this solution is constant, O(1)
'''

def find_max_sum_sub_array(nums):
    if len(nums) < 1:
        return 0
    curr_max = nums[0]
    global_max = nums[0]
    len_nums = len(nums)
    for i in range(1, len_nums):
        if curr_max < 0:
            curr_max = nums[i]
        else:
            curr_max += nums[i]

        if global_max < curr_max:
            global_max = curr_max

    return global_max

if __name__ == "__main__":
    v = [-4, 2, -5, 1, 2, 3, 6, -5, 1]
    sum_v = find_max_sum_sub_array(v)
    print(f'Sum of largest subarray: {str(sum_v)}')