def lcq_recursive(seq1, seq2, idx1=0, idx2=0):
    # Check if either of the sequences is exhausted
    if idx1 == len(seq1) or idx2 == len(seq2):
        return 0

    # Check if the current characters are equal
    if seq1[idx1] == seq2[idx2]:
        return 1 + lcq_recursive(seq1, seq2, idx1 + 1, idx2 + 1)
    # Skip one element from each sequence
    else:
        return max(lcq_recursive(seq1, seq2, idx1 + 1, idx2),
                   lcq_recursive(seq1, seq2, idx1, idx2 + 1))


def lcq_memoized(seq1, seq2):
    memo = {}

    def recurse(idx1, idx2):
        key = idx1, idx2

        if key in memo:
            return memo[key]

        if idx1 == len(seq1) or idx2 == len(seq2):
            memo[key] = 0
        elif seq1[idx1] == seq2[idx2]:
            memo[key] = 1 + recurse(idx1 + 1, idx2 + 1)
        else:
            memo[key] = max(recurse(idx1 + 1, idx2),
                            recurse(idx1, idx2 + 1))
        return memo[key]

    return recurse(0, 0)


def lcq_dp(seq1, seq2):
    n1, n2 = len(seq1), len(seq2)
    results = [[0 for _ in range(n2+1)] for _ in range(n1+1)]
    for idx1 in range(n1):
        for idx2 in range(n2):
            if seq1[idx1] == seq2[idx2]:
                results[idx1+1][idx2+1] = 1 + results[idx1][idx2]
            else:
                results[idx1+1][idx2+1] = max(results[idx1][idx2+1], results[idx1+1][idx2])
    return results[-1][-1]


def max_profit_recursive(capacity, weights, profits, idx=0):
    if idx == len(weights):
        return 0
    if weights[idx] > capacity:
        return max_profit_recursive(capacity, weights, profits, idx+1)
    else:
        return max(max_profit_recursive(capacity, weights, profits, idx+1),
                   profits[idx] + max_profit_recursive(capacity-weights[idx], weights, profits, idx+1))


def knapsack_memo(capacity, weights, profits):
    memo = {}

    def recurse(idx, remaining):
        key = (idx, remaining)
        if key in memo:
            return memo[key]
        elif idx == len(weights):
            memo[key] = 0
        elif weights[idx] > remaining:
            memo[key] = recurse(idx + 1, remaining)
        else:
            memo[key] = max(recurse(idx + 1, remaining),
                            profits[idx] + recurse(idx + 1, remaining - weights[idx]))
        return memo[key]

    return recurse(0, capacity)


def knapsack_dp(capacity, weights, profits):
    n = len(weights)
    results = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for idx in range(n):
        for c in range(capacity + 1):
            if weights[idx] > c:
                results[idx + 1][c] = results[idx][c]
            else:
                results[idx + 1][c] = max(results[idx][c], profits[idx] + results[idx][c - weights[idx]])

    return results[-1][-1]