class Book:
	def __init__(self, title, author, year, pages, id):
		self._title = title
		self._author = author
		self._year = year
		self.pages = pages
		self.__id = id

	def info(self):
		return f"{self._title} - {self._author} ({self._year}), {self.pages} стр."

	def read(self):
		return f"Читаю книгу \"{self._title}\""

	def has_read(self):
			return f"Книга \"{self._title}\" прочитана"
	
	def get_id(self):
		return self.__id


class AudioBook(Book):
	def __init__(self, title, author, year, pages, id, narrator, duration):
		super().__init__(title, author, year, pages, id)
		self.narrator = narrator
		self.duration = duration

	def read(self):
		return f"Слушаю книгу \"{self._title}\""

	def has_read(self):
		return f"Книга \"{self._title}\" прослушана, актер озвучки - {self.narrator}"

book1 = Book("Убийство Роджера Экройда", "Агата Кристи", 1926, 320, "FHJ305")
print("## Первая книга супер класса Ebook ##")
print(book1.info())
print(book1.read())
print(book1.get_id())
print("####################")
book2 = AudioBook("Убийство Роджера Экройда", "Агата Кристи", 1926, 320, "FHJ305", "Васильев Никита", 210)
print("## Вторая книга наследника AudioBook ##")
print(book2.info())
print(book2.read())