"""Comma Code."""

spam = ['apples', 'bananas', 'tofu', 'cats']


def list_joiner(list):
    """Take a list and print it as an Oxford comma having sentence."""
    count = 0
    joined = ''
    while count < len(list) - 2:
        joined += list[count] + ', '
        count += 1
    joined += list[-2] + ' and '
    joined += list[-1] + '.'
    return joined


print(list_joiner(spam))
