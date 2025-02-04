import random
import re


def generate_password(password_lenth):

    small_letters = 'abcdefghijkmnpqrstuvwxyz'
    big_letters = 'ABCDEFGHJKLMNPQRSTUVWXYZ'
    numbers = '123456789123456789'
    symbols = '!@#$%^&*()_-+~`=:;?,.{}[]'
    chars = big_letters + small_letters + numbers + symbols

    if password_lenth < 5:
        password_size = 5
    elif password_lenth > 64:
        password_size = 64
    else:
        password_size = password_lenth

    def generate_random_string(size, str):
        result = ''
        for i in range(size):
            result += random.choice(chars)

        return result

    num_pattern = r'[0-9]'
    big_char_pattern = r'[A-Z]'
    small_char_pattern = r'[a-z]'
    symbol_pattern = r'[/!/@/#/$/%/^/&/*/(/)/_/-/+/~/`/=/:/;?/,/./{/}/|/[/]]'

    def is_exist(pattern, text):
        return re.search(pattern, text) is not None

    def is_valid(str):
        nu = (re.search(num_pattern, str) is not None)
        bi = (re.search(big_char_pattern, str) is not None)
        sm = (re.search(small_char_pattern, str) is not None)
        sy = (re.search(symbol_pattern, str) is not None)

        return nu and bi and sm and sy

    iterations = 1
    password = None
    while True:
        random_chars = generate_random_string(len(chars), chars)
        password = generate_random_string(password_size, random_chars)
        if is_valid(password):
            break
        iterations += 1

    print("_________________________________")
    print(f"Количество иттераций = {iterations}")
    print(f"random_chars = {random_chars}")
    return password

passwd = generate_password(0)

print("_________________________________")
print(f"Пароль: {passwd}")
print(f"Длинв пароля: {len(passwd)}")
print("_________________________________")
