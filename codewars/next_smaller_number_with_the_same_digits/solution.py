# TODO improve asymptotic complexity
from itertools import permutations


def next_smaller(n):
    digits_of_n = [digit for digit in str(n)]
    digit_permutations = [int(''.join(num)) for num in list(permutations(digits_of_n)) if num[0] != '0']
    lower_nums = [num for num in digit_permutations if num < n]
    return max(lower_nums) if lower_nums else -1


print(next_smaller(9))
print(next_smaller(123456798))
