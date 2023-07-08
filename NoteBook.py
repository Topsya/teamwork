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



if __name__ == "__main__":
    zapis = input('add new notes: ')




