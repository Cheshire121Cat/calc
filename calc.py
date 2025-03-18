def calculator():
  """Простой калькулятор, поддерживающий сложение, вычитание, умножение и деление."""

  try:
    num1 = float(input("Введите первое число: "))
    operator = input("Введите оператор (+, -, *, /): ")
    num2 = float(input("Введите второе число: "))

    if operator == '+':
      result = num1 + num2
    elif operator == '-':
      result = num1 - num2
    elif operator == '*':
      result = num1 * num2
    elif operator == '/':
      if num2 == 0:
        print("Ошибка! Деление на ноль невозможно.")
        return  # Выход из функции, если деление на ноль
      result = num1 / num2
    else:
      print("Неверный оператор.  Используйте +, -, *, /")
      return  # Выход из функции, если оператор недействителен

    print("Результат:", result)

  except ValueError:
    print("Ошибка! Введите корректные числа.")
  except Exception as e:
    print(f"Произошла непредвиденная ошибка: {e}")


if __name__ == "__main__":
  calculator()
