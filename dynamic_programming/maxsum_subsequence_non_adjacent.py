'''
find the maximum sum of a subsequence in an array so
that no consecutive elements are part of this subsequence.
'''

def maxsum_nonadjacent(a):
    if len(a) < 3:
        if a[0] + a[2] > a[1]:
            return a[0] + a[2]
        else:
            return a[1]
    sum1 = max(a[2], 0) + max(a[0], 0)
    sum0 = max(a[1], 0)
    sum_i = max(a[0], 0)
    for i in range(3, len(a)):
        # sim_i = max(sum0,sum1)
        new_s = sum0 + max(a[i], 0)
        new_s_i = sum_i + max(a[i], 0)
        sum_i = max(sum_i, sum0)
        sum0 = max(new_s, new_s_i)
        sum0, sum1 = sum1, sum0
    return max(sum0, sum1, sum_i)

if __name__ == "__main__":
    v = [1, 16, 10, 14, 60, -5, 6, -5, 1]
    sum_v = maxsum_nonadjacent(v)
    print(f'Sum of largest subarray: {str(sum_v)}')