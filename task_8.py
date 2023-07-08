class NoteBook:
    # предыдущие функции
    pass

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
