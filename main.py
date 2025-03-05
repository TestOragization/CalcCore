def core_calculator():
    while True:
        expr = input("Введите выражение ('exit' для выхода): ")
        if expr.lower() == "exit":
            print("Программа завершена.")
            break
        try:
            result = eval(expr)
            print(f"Результат: {result}")
        except Exception as e:
            print(f"Ошибка: {e}")

if __name__ == "__main__":
    core_calculator()
