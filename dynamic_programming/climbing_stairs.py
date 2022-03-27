'''
You are climbing a staircase that has n steps.
You can take the steps either 1 or 2 at a time.
Calculate how many distinct ways you can climb to the top of the staircase.
'''

def solution(n):
    def climb_staircase(k,cache):
        if k<=0:
            return 0
        if k==1:
            return 1
        elif k ==2:
            return 2
        if k in cache:
            return cache[k]
        steps = climb_staircase(k-1,cache) + climb_staircase(k-2,cache)
        cache[k] = steps
        return steps
    cache = {}
    return climb_staircase(n,cache)