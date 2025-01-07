from calculator import Calculator
from file_browser import FileBrowser


def main():
    print("========================================")
    print("|       Program stworzony przez:       |")
    print("|           Aleksander Bystrek         |")
    print("|  Github: https://github.com/kerbi404 |")
    print("========================================")
    print("------------ GŁÓWNY PROGRAM ------------")
    print("Dostępne polecenia: 'calc' - Kalkulator, 'files' - Przeglądarka plików, 'quit' - Wyjście")

    #klasy calc i filebrowser
    calc = Calculator()
    fb = FileBrowser()

    while True:
        command = input("\nWpisz komendę: ").strip().lower()

        if command == 'quit':
            #wyjscie
            print("Zamykam program. Do widzenia!")
            break
        elif command == 'calc':
            #wejscie w kalkulator
            print("------------ KALKULATOR ------------")
            calc.run()
            print("------------ KONIEC KALKULATORA ------------")
        elif command == 'files':
            #wejscie w przegladarke plikow
            print("------------ PRZEGLĄDARKA PLIKÓW ------------")
            fb.run()
            print("------------ KONIEC PRZEGLĄDARKI PLIKÓW ------------")
        else:
            print("Nieprawidłowa komenda. Spróbuj 'calc', 'files', lub 'quit'")


if __name__ == "__main__":
    main()