import random


def generate_list():
    return random.sample(range(1, 10000), random.randint(5, 15))


def get_evens(nums):
    return list(filter(lambda x: x % 2 == 0, nums))
