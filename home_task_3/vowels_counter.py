import re


message = input("Введите любое слово или фразу :")
vowels_pattern = r'[аАеЕёЁиИоОуУыЫэЭюЮяЯaAeEiIoOuUyY]'
vowels_chars = re.findall(vowels_pattern, message)
print(vowels_chars)
if vowels_chars is not None:
    print(f"Количество гласных букв = {len(vowels_chars)}")
else:
    print("Гласных букв в веденной фразе НЕТ!")