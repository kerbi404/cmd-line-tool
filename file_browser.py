import os

class FileBrowser:
    def __init__(self):
        #ustawienie poczatkowej sciezki na biezacy katalog
        self.current_path = os.getcwd()

    def run(self):
        while True:
            print("\nDostępne polecenia: 'ls', 'cd <ścieżka>', 'pwd', 'head <plik>', 'q' aby wyjść")
            command = input("Podaj komendę: ").strip().lower()

            if command == 'q':
                #wyjscie z przegladarki plikow
                print("Zamykam przeglądarkę plików.")
                break
            elif command == 'ls':
                #wiswietlanie plikow
                print("------------ LISTA PLIKÓW ------------")
                self.list_files()
            elif command.startswith('cd '):
                #zmiana katalogu na podany przez uzytkownika
                path = command[3:].strip()
                self.change_directory(path)
            elif command == 'pwd':
                #podanie biezacej sciezki w ktorej jest uzytkownik
                print("------------ AKTUALNA ŚCIEŻKA ------------")
                self.print_working_directory()
            elif command.startswith('head '):
                #512b
                filename = command[5:].strip()
                print(f"------------ ZAWARTOŚĆ PLIKU: {filename} ------------")
                self.print_file_head(filename)
            else:
                #errory
                print("Nieprawidłowa komenda. Spróbuj ponownie.")

    def list_files(self):
        #wyswietlanie plikow i katalogow w biezacym pliku
        try:
            for file in os.listdir(self.current_path):
                print(file)
        except Exception as e:
            print(f"Błąd podczas wyświetlania plików: {e}")

    def change_directory(self, path):
        #zmiana katalogu
        try:
            os.chdir(path)
            self.current_path = os.getcwd()
            print(f"Zmieniono katalog na: {self.current_path}")
        except FileNotFoundError:
            print("Błąd: Katalog nie istnieje.")
        except Exception as e:
            print(f"Błąd: {e}")

    def print_working_directory(self):
        #wyswietlenie sciezki
        print(f"Obecny katalog: {self.current_path}")

    def print_file_head(self, filename):
        #512b
        try:
            file_path = os.path.join(self.current_path, filename)
            with open(file_path, "r", encoding="utf-8") as file:
                print(file.read(512))
        except FileNotFoundError:
            print("Błąd: Plik nie został znaleziony.")
        except PermissionError:
            print("Błąd: Brak dostępu do pliku.")
        except UnicodeDecodeError:
            print("Błąd: Nie można odczytać pliku - nieobsługiwane kodowanie.")
        except Exception as e:
            print(f"Nieoczekiwany błąd: {e}")