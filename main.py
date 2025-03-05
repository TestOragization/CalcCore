import pyodbc
from datetime import datetime


class Calculator:
    def __init__(self):
        self.history = []
        self.connection_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=CalculatorApp;Trusted_Connection=yes'
        self.conn = pyodbc.connect(self.connection_string)
        self.cursor = self.conn.cursor()

    def calculate(self, expression: str):
        try:
            result = eval(expression)
            self.store_history(expression, result)
            self.user_logs(expression, result)
            return result

        except Exception as e:
            return f"Ошибка: {e}"

    def user_logs(self, action, result):
        query = "INSERT INTO UserLogs (Action, Result) VALUES (?, ?)"
        self.cursor.execute(query, (action, str(result)))
        self.conn.commit()