# 1-masala
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def info(self):
        print(f"Nom: {self.title}, Muallif: {self.author}")

class Library(Book):
    def __init__(self,name, kitoblar = []):
        self.name = name
        self.kitoblar = kitoblar

    def kitob_qow(self, kitob):
        self.kitoblar.append(kitob)

    def library_info(self):
        print(f"{self.name} kutubxonasining kitoblari")
        for k in self.kitoblar:
            k.info()
        print()

b1 = Book("O'tgan kunlar", "Abdulla Qodiriy")
b2 = Book("Mehrobdan chayon", "Abdulla Qodiriy")
b3 = Book("Sariq devni minib", "Xudoyberdi To'xtaboyev")

roy = [b1, b2, b3]

kutubxona = Library("A.Navoiy", roy)
kutubxona.library_info()
