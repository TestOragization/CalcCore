class Calculator:
    def __init__(self):
        self.history = []

    def calculate(self, expression: str):
        try:
            result = eval(expression)
            self.history.append(f"{expression} = {result}")
            return result
        except Exception as e:
            return f"Ошибка: {e}"

    def show_history(self):
        if self.history:
            print("История расчетов:")
            for entry in self.history:
                print(entry)
        else:
            print("История пуста.")

class CoreCalculator:
    def __init__(self):
        self.calculator = Calculator()

    def start(self):
        while True:
            expr = input("Введите выражение ('exit' для выхода, 'history' для истории): ")
            if expr.lower() == "exit":
                print("Программа завершена.")
                break
            elif expr.lower() == "history":
                self.calculator.show_history()
            else:
                result = self.calculator.calculate(expr)
                print(f"Результат: {result}")

if __name__ == "__main__":
    core = CoreCalculator()
    core.start()
