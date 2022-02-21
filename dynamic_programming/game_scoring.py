#Question: A game where a player can score 1,2, or 4 runs. Given a score, n, find the total number of ways to score n runs.
#memoization
'''
The runtime complexity of this solution is linear, O(n).
The memory complexity of this solution is linear, O(n).
Memoization is an optimization technique used to make programs faster and improve their performance by storing the
results of expensive function calls and returning the cached result when the same input occurs again.
It saves the computed results for possible later reuse, rather than recomputing them.
'''


def scoring_options(n):
    cache = {}
    cache[0] = 1
    num = scoring_rec_memoization(n,cache)
    return num
def scoring_rec_memoization(n,cache):
    if n<0:
        return 0
    if n in cache:
        return cache[n]
    cache[n] = scoring_rec_memoization(n-1,cache) + scoring_rec_memoization(n-2,cache) + scoring_rec_memoization(n-4,cache)
    return cache[n]
if __name__ == "__main__":
    n=10
    num_ways_to_score = scoring_options(n)
    print(f'player can score the {n} in {num_ways_to_score} ways')