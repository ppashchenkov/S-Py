items_list = ["Фильмы", "Спектакли", "Фитнес"]

def print_list(list):
    n = 1
    print("Мне нравится:")
    for item in list:
        print(f"{n}. {item}")
        n += 1

while True:
    try:
        range_num = int(input("Введите целое число от 0 до 5:"))
        if 5 >= range_num >= 0:
            print_list(items_list)
            break
        else:
            print("Число вне указанного диапазона!")
    except Exception as e:
        print("ОШИБКА!!!")
        print(e)
