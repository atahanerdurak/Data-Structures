from jovian.pythondsa import evaluate_test_cases

tests = [{
    "input": {
        "cards": [13, 11, 10, 7, 4, 3, 1, 0],
        "query": 7
    },
    "output": 3
}, {
    "input": {
        "cards": [13, 11, 10, 7, 4, 3, 1, 0],
        "query": 1
    },
    "output": 6
}, {
    "input": {
        "cards": [4, 2, 1, -1],
        "query": 4
    },
    "output": 0
}, {
    "input": {
        "cards": [3, -1, -9, -127],
        "query": -127
    },
    "output": 3
}, {
    "input": {
        "cards": [6],
        "query": 6
    },
    "output": 0
}, {
    "input": {
        "cards": [9, 7, 5, 2, -9],
        "query": 4
    },
    "output": -1
}, {
    "input": {
        "cards": [],
        "query": 7
    },
    "output": -1
}, {
    "input": {
        "cards": [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        "query": 3
    },
    "output": 7
}, {
    "input": {
        "cards": [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        "query": 6
    },
    "output": 2
}]


def locate_card0(cards, query):  # LINEAR SEARCH ALGORITHM
    position = 0
    while position < len(cards):
        if cards[position] == query:
            return position
        position += 1
    return -1


# def test_location(cards, query, mid):
#     if cards[mid] == query:
#         if mid - 1 >= 0 and cards[mid - 1] == query:
#             return "left"
#         else:
#             return "found"
#     elif cards[mid] < query:
#         return "left"
#     else:
#         return "right"
#
#
# def locate_card(cards, query):
#     lo = 0
#     hi = len(cards) - 1
#     while lo <= hi:
#         mid = (lo + hi) // 2
#         result = test_location(cards, query, mid)
#
#         if result == "found":
#             return mid
#         elif result == "left":
#             hi = mid - 1
#         elif result == "right":
#             lo = mid + 1
#
#     return -1

def locate_card(cards, query):
    lo, hi = 0, len(cards) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if cards[mid] == query and cards[mid] == cards[mid-1] and mid-1 >= 0:
            hi = mid - 1
        elif cards[mid] < query:
            hi = mid - 1
        elif cards[mid] > query:
            lo = mid + 1
        else:
            return mid

    return -1


def binary_search(lo, hi, condition): # binary search for first and last position
    while lo <= hi:
        mid = (lo + hi) // 2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        else:
            lo = mid + 1
    return -1


def first_position(nums, target):  # finding condition and putting in binary search for first position
    def condition(mid):
        if nums[mid] == target:
            if mid > 0 and nums[mid-1] == target:
                return 'left'
            return 'found'
        elif nums[mid] < target:
            return 'right'
        else:
            return 'left'
    return binary_search(0, len(nums)-1, condition)


def last_position(nums, target):  # finding condition and putting in binary search for last position
    def condition(mid):
        if nums[mid] == target:
            if mid < len(nums)-1 and nums[mid+1] == target:
                return 'right'
            return 'found'
        elif nums[mid] < target:
            return 'right'
        else:
            return 'left'
    return binary_search(0, len(nums)-1, condition)


def first_and_last_position(nums, target):
    return first_position(nums, target), last_position(nums, target)


result = locate_card(**tests[1]["input"])

print(result)
evaluate_test_cases(locate_card, tests)
