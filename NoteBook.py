from datetime import datetime


now = datetime.now()


class Notatki:
    def __init__(self, zapis, now):
        self.zapis = zapis + now


class NoteBook:
    def __init__(self):
        self.notatki = []

    def add_notatki(self, notatki):
        self.notatki.append(notatki)


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
    zapis = input('add new notes: ')
