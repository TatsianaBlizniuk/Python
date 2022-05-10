# Kласс Book: id, Название, Автор (ы), Издательство, Год издания, Количество страниц, Цена, Тип переплета.
# Создайте класс и поля соответствующему вашему варианту (поля статические и динамические).
# Создайте три метода (класса, объекта и статический).
# Выберете поле или метод для реализации инкапсуляции.
# Пропишите запись и считывание (get, set) инкапсулированных полей.

class Book:
    count = 0
    _id = 0

    def __init__(self, name, author, pub_house, year, number_pages, price, binding_type):
        self._id = Book.count + 1
        self.name = name
        self.author = author
        self.publishing_house = pub_house
        self.year = year
        self.number_of_pages = number_pages
        self.price = price
        self.binding_type = binding_type
        Book.count += 1

    def __del__(self):
        Book.count -= 1

    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id

    # Статические методы:
    def price_hash(price):
        if price == '50':
            print("Дорого")
        elif price == '35':
            print("Неплохо")
        else:
            print("Хорошо")

    @classmethod
    def total(cls):
        print(f"Total books: {cls.count}")

    def show(self):
        text = ""
        if self.name != None: text = text + self.name[0:50] + ", "
        if self.author != None: text = text + self.author[0:50] + " "
        if self.binding_type != None: text = text + self.binding_type[0:50] + "    "
        print(text)

b1 = Book('Щегол', 'Донна Тартт', 'Росмэн', 2020, 750, 45, 'Твердый переплет')
b2 = Book('Щелкунчик', 'Гофман', 'Росмэн', 2022, 48, 22, 'Твердый переплет')
b3 = Book('Бестолковый буклетик', 'Автор неизвестен', 'Рога и копыта', 2022, 4, 1, 'Мягкий переплет')

b1.show()
b2.show()
b3.show()

Book.total()

b1.set_id(10)
b2.set_id(25)
b3.set_id(30)
print(b2.get_id())