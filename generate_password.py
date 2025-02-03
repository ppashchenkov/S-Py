import random


def generate_password(password_lenth):

    small_letters = 'abcdefghijklmnopqrstuvwxyz'
    big_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!@#$%^&*()_-+~`=:;?,.{}|[]'
    chars = big_letters + small_letters + numbers + symbols

    if password_lenth < 4:
        password_size = 4
    elif password_lenth > 64:
        password_size = 64
    else:
        password_size = password_lenth

    def generate_random_string(size, str):
        result = ''
        for i in range(size):
            result += random.choice(chars)

        return result

    # def all_cases(string):
    #     upper = / [A - Z] /.test(string)


    return generate_random_string(password_size, chars)

passwd = generate_password(14)

print("_________________________________")
print(f"Пароль: {passwd}")
print(f"Длинв пароля: {len(passwd)}")
print("_________________________________")
