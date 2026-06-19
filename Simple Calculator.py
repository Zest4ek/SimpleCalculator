print("Simple Calculator v1.0")

num = int(input("Введите число от 0 до 100: "))
num2 = int(input("Введите другое число от 0 до 100: "))
sign = input("Выберите операцию с числами (+, -, *, /): ")

if num < 0 or num > 100 or num2 < 0 or num2 > 100:
    print("Числа выходят за область допустимых значений!")
elif num2 == 0:
    print("На ноль делить нельзя!")
    exit()

print("Вычисляю...")