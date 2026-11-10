# 19 задание
class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount


# 20 задание
class User:
    def __init__(self, password):
        self.__password = password

    def check_password(self, password):
        return self.__password == password


# 21 задание
class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount

    def get_balance(self):
        return self._balance


# 22 задание
class Temperature:
    def __init__(self, celsius):
        self.__celsius = celsius

    @property
    def celsius(self):
        return self.__celsius

    @celsius.setter
    def celsius(self, value):
        if value >= -273.15:
            self.__celsius = value
        else:
            raise ValueError("Температура ниже абсолютного нуля")


# 23 задание
class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value >= 0:
            self.__price = value
        else:
            raise ValueError("Цена не может быть отрицательной")


# 24 задание
class Age:
    def __init__(self, age):
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if 0 <= value <= 120:
            self.__age = value
        else:
            raise ValueError("Возраст должен быть от 0 до 120")


# 25 задание
class Playlist:
    def __init__(self):
        self._songs = []

    def add_song(self, song):
        self._songs.append(song)

    def remove_song(self, song):
        if song in self._songs:
            self._songs.remove(song)


# 26 задание
class Thermostat:
    def __init__(self, temperature):
        self.__target_temperature = temperature

    @property
    def target_temperature(self):
        return self.__target_temperature

    @target_temperature.setter
    def target_temperature(self, value):
        if 16 <= value <= 30:
            self.__target_temperature = value
        else:
            raise ValueError("Температура должна быть от 16 до 30")


# 27 задание
class Wallet:
    def __init__(self, balance=0):
        self.__balance = balance

    def add_money(self, amount):
        if amount > 0:
            self.__balance += amount

    def spend_money(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount


# 28 задание
class Email:
    def __init__(self, address):
        self.address = address

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):
        if "@" in value:
            self.__address = value
        else:
            print("Ошибка: адрес должен содержать @")


# 29 задание
class Car:
    def __init__(self, fuel_level):
        self._fuel_level = fuel_level

    def refuel(self, amount):
        if amount > 0:
            self._fuel_level = min(100, self._fuel_level + amount)

    def drive(self, amount):
        if 0 <= amount <= self._fuel_level:
            self._fuel_level -= amount


# 30 задание
class SecureNote:
    def __init__(self, content, password):
        self.__content = content
        self.__password = password

    def reveal(self, password):
        if password == self.__password:
            return self.__content
        else:
            return "Неверный пароль"



        # Проверка заданий (вывод результатов в терминал)

# 19 и 21 задание
account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
print("Баланс банка:", account.get_balance())

# 20 задание
user = User("12345")
print("Пароль верный:", user.check_password("12345"))

# 22 задание
temp = Temperature(25)
print("Температура:", temp.celsius)

# 23 задание
product = Product(1500)
print("Цена товара:", product.price)

# 24 задание
age = Age(20)
print("Возраст:", age.age)

# 25 задание
playlist = Playlist()
playlist.add_song("Song 1")
playlist.add_song("Song 2")
playlist.remove_song("Song 1")
print("Плейлист:", playlist._songs)

# 26 задание
thermostat = Thermostat(22)
print("Температура термостата:", thermostat.target_temperature)

# 27 задание
wallet = Wallet(5000)
wallet.add_money(1000)
wallet.spend_money(2000)
print("Деньги в кошельке:", wallet._Wallet__balance)

# 28 задание
email = Email("test@gmail.com")
print("Email:", email.address)

# 29 задание
car = Car(80)
car.drive(30)
car.refuel(20)
print("Топливо в машине:", car._fuel_level)

# 30 задание
note = SecureNote("Моя секретная заметка", "1234")
print("Заметка:", note.reveal("1234"))