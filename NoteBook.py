from datetime import datetime


now = datetime.now()


class Notatki:
    def __init__(self, zapis, now):
        self.zapis = zapis + now.strftime(" %Y-%m-%d %H:%M:%S")


class NoteBook:
    def __init__(self):
        self.notatki = []

    def add_notatki(self, notatki):
        self.notatki.append(notatki)

    def search_notatki(self, keyword):
            found_notatki = []
            for notatka in self.notatki:
                if keyword in notatka.zapis:
                    found_notatki.append(notatka)
            return found_notatki

    def edit_notatki(self, index, notatki):
        if index >= 0 and index < len(self.notatki):
            self.notatki[index] = notatki
        else:
            raise IndexError("Invalid note index")

    def delete_notatki(self, index):
        if index >= 0 and index < len(self.notatki):
            del self.notatki[index]
        else:
            raise IndexError("Invalid note index")


if __name__ == "__main__":
    notebook = NoteBook()

    zapis = input('add new notes: ')
    notebook.add_notatki(Notatki(zapis, now))

    search_keyword = input('enter search keyword: ')
    found_notatki = notebook.search_notatki(search_keyword)
    if found_notatki:
        print("Found notatki:")
        for notatka in found_notatki:
            print(notatka.zapis)
    else:
        print("No notatki found.")
