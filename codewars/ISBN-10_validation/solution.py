def valid_ISBN10(isbn):
    # check length
    if len(isbn) != 10:
        return False

    # check first 9 characters are numbers
    if not isbn[:9].isnumeric():
        return False

    # check final character either number or 'X'
    if not (isbn[9].isnumeric() or isbn[9] == 'X'):
        return False

    # check (sum of (digit * position)) modulo 11 equals zero
    return (sum([(i + 1) * int(char) for i, char in enumerate(isbn[:-1])]) +
            (int(isbn[9]) if isbn[9] != 'X' else 10) * 10) % 11 == 0


print(valid_ISBN10('1112223339'))
