def add(a,b):
    #возвращает сумму a и b
    return a+b
def subtract(a,b):
    #возвращает разницу а и б
    return a-b
def multiply(a,b):
    #вовращает умножение а на б
    return a*b
def divide(a,b):
    #возвращает деление а на б
    if b == 0:
        raise ValueError ("Деление на ноль невозможно")
    return a/b
# a=float(input("Первое число: "))
# b=float(input("Второе число: "))
# operation=input("Операция(+,-,*,/): ")
# if operation == "+":
#     print(add(a,b))
# elif operation == "-":
#     print(subtract(a,b))
# elif operation == "*":
#     print(multiply(a,b))
# elif operation == "/":
#     print(divide(a,b))
# else:
#     print("Неверный ввод")