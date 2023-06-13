from jovian.pythondsa import evaluate_test_cases

test0 = {
    'input': {
        'nums': [19, 25, 29, 3, 5, 6, 7, 9, 11, 14]
    },
    'output': 3
}

test1 = {
    'input': {
        'nums': [4, 5, 6, 7, 8, 1, 2, 3]
    },
    'output': 5
}

test2 = {
    'input': {
        'nums': [1, 2, 3, 4, 5]
    },
    'output': 0
}

test3 = {
    'input': {
        'nums': [5, 1, 2, 3, 4]
    },
    'output': 1
}

test4 = {
    'input': {
        'nums': [2, 3, 4, 5, 1]
    },
    'output': 4
}

test5 = {
    'input': {
        'nums': [1, 2, 3, 4, 5]
    },
    'output': 0
}

test6 = {
    'input': {
        'nums': []
    },
    'output': -1
}

test7 = {
    'input': {
        'nums': [1]
    },
    'output': 0
}

tests = [test0, test1, test2, test3, test3, test5, test6, test7]


def count_rotations_linear(nums):
    position = 0  # What is the initial value of position?
    if len(nums) == 0:
        return -1
    while position < len(nums) - 1:  # When should the loop be terminated?

        # Success criteria: check whether the number at the current position is smaller than the one before it
        if nums[position + 1] < nums[position]:  # How to perform the check?
            return position + 1

        # Move to the next position
        position += 1

    return 0


def count_rotations_binary(nums):
    if len(nums) == 0:
        return -1

    lo = 0
    hi = len(nums) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        if mid > 0 and nums[mid] < nums[mid - 1]:
            return mid
        elif nums[hi] > nums[mid]:
            hi = mid - 1
        else:
            lo = mid + 1

    return 0


linear_search_result = evaluate_test_cases(count_rotations_linear, tests)

binary_search_result = evaluate_test_cases(count_rotations_binary, tests)
