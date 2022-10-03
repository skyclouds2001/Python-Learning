from random import randint


def get_random_character(ch1, ch2):
    return chr(randint(ord(ch1), ord(ch2)))


def get_random_lower_case_letter():
    return get_random_character('a', 'z')


def get_random_upper_case_letter():
    return get_random_character('A', 'Z')


def get_random_digit_character():
    return get_random_character('0', '9')


def get_random_ascii_character():
    return chr(randint(0, 127))
