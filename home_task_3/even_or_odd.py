n = 0
while True:
    try:
        n = int(input("Введите целое число: "))
        break
    except Exception as e:
        print(e)
        print("ОШИБКА! Повторите ввод целого числа")

if n % 2 == 0: print("четное")
else: print("нечетное")
