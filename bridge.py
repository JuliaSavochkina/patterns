"""
Bridge или мост.
Применение:
    - требуется избежать постоянной привязки абстракции к реализации;
    - и абстракции, и реализации должны расширяться новыми подклассами;
    - изменения в реализации абстракции не должны отражаться на клиентах;
    - число классов стремительно разрастается;
    - реализация должна совместно использоваться несколькими объектами.

Результаты:
    - отделение реализации от интерфейса;
    - повышение степени расширяемости;
    - сокрытие деталей реализации от клиентов.
"""


# Passenger & Cargo Carriers

class Carrier:
    def carry_military(self, items):
        pass

    def carry_commercial(self, items):
        pass


class Cargo(Carrier):
    def carry_military(self, items):
        print("The plane carries ", items, " military cargo goods")

    def carry_commercial(self, items):
        print("The plane carries ", items, " commercial cargo goods")


class Passenger(Carrier):
    def carry_military(self, passengers):
        print("The plane carries ", passengers, " military passengers")

    def carry_commercial(self, passengers):
        print("The plane carries ", passengers, " commercial passengers")


# Military & Commercial Planes
class Plane:
    def __init__(self, Carrier):
        self.carrier = Carrier

    def display_description(self):
        pass

    def add_objects(self):
        pass


class Commercial(Plane):
    def __init__(self, Carrier, objects):
        super().__init__(Carrier)
        self.objects = objects

    def display_description(self):
        self.carrier.carry_commercial(self.objects)

    def add_objects(self, new_objects):
        self.objects += new_objects


class Military(Plane):
    def __init__(self, Carrier, objects):
        super().__init__(Carrier)
        self.objects = objects

    def display_description(self):
        self.carrier.carry_military(self.objects)

    def add_objects(self, new_objects):
        self.objects += new_objects


cargo = Cargo()
passenger = Passenger()

# Bridging Military and Cargo classes
military1 = Military(cargo, 100)
military1.display_description()
military1.add_objects(25)
military1.display_description()

"""Здесь мы создали экземпляры объектов для классов Cargo и Passenger.
Затем в вызове конструктора класса Military мы передали экземпляр cargo.
Поскольку это военный самолет, груз считается военным грузом.

Поэтому метод display_description() выведет на печать сведения о военном грузе.
Кроме того, мы добавили еще один 25 объекты поверх этой нагрузки:

>>> The plane carries 100 military cargo goods
>>> The plane carries 125 military cargo goods
"""