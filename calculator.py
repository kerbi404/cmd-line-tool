import math

class Calculator:
    def __init__(self):
        #plik do zapisywania historii korzystania z kalkulatora
        self.history_file = "calc_history.txt"

    def run(self):
        while True:
            print("\nWybierz operację: '+', '-', '*', '/', '!', '^' lub 'q' aby wyjść")
            operation = input("Wybierz operację: ").strip()

            if operation == 'q':
                #wyjscie
                print("Zamykam kalkulator.")
                break

            try:
                if operation in ['+', '-', '*', '/']:
                    #operacje wymagajace dwoch liczb
                    num1 = float(input("Wpisz pierwszą liczbę: "))
                    num2 = float(input("Wpisz drugą liczbę: "))
                    result = self.calculate(operation, num1, num2)
                elif operation == '!':
                    #operacja silni (tylko dla intow)
                    num = int(input("Wpisz liczbę: "))
                    if num < 0:
                        raise ValueError("Silnia nie jest zdefiniowana dla liczb ujemnych.")
                    result = math.factorial(num)
                elif operation == '^':
                    #potegowanie (skladnia i^ wykladnik)
                    base = float(input("Wpisz liczbę: "))
                    exponent = float(input("Wpisz wykładnik: "))
                    result = math.pow(base, exponent)
                else:
                    #tu jak cos zle
                    print("Nieznana operacja. Spróbuj ponownie.")
                    continue

                print(f"Wynik: {result}")
                #zapisywanie wynikow do pliku
                self.save_history(operation,(num1 if 'num1' in locals() else None, num2 if 'num2' in locals() else None), result)
            except ValueError as ve:
                print(f"Błąd: {ve}")
            except ZeroDivisionError:
                print("Błąd: Nie można dzielić przez zero.")
            except Exception as e:
                print(f"Nieoczekiwany błąd??: {e}")

    def calculate(self, operation, num1, num2):
        #polecenia i returny z wynikami
        if operation == '+':
            return num1 + num2
        elif operation == '-':
            return num1 - num2
        elif operation == '*':
            return num1 * num2
        elif operation == '/':
            return num1 / num2

    def save_history(self, operation, numbers, result):
        #zapisanie operacji do pliku historii
        with open(self.history_file, "a") as file:
            file.write(f"{operation} {numbers} = {result}\n")