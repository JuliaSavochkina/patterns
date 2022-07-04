"""
Abstact Factory или абстрактная фабрика.
Условия применения:
    - система не должна зависить от того, как создаются, компонуются и представляются входящие в нее объекты;
    - система должна настраиваться одним из семейств объектов;
    - входящие в семейство взаимосвязанные объекты спроектированы для совместной работы, и должно обеспечить выполнение
    этого ограничения;
    - есть необходимость предоставить библиотеку объектов, раскрывая только их интерфейсы, но не реализацию.

Паттерн позволяет:
    - изолировать конкретные классы;
    - упрощает замену семейств продуктов;
    - гарантирует сочетаемость продуктов;
    - не упрощать задачу поддержки нового вида продуктов.
"""

from abc import ABC, abstractmethod

class AbstractClass(ABC):
    @abstractmethod
    def func(self):
        pass

class ChildClass(AbstractClass):
    def func(self):
        out = "This is an output"
        return out

obj = ChildClass()
print(obj.func())

# ================ПРИМЕР==================

class WindowFactory:
    @classmethod
    def create_window(cls, name):
    """Метод создания окна, возврашает класс окно"""
        return cls.Window(name)
    @classmethod
    def create_button(cls, name):
    """Метод создания кнопки, возврашает класс кнопки"""
        return cls.Button(name)


class MacOsFactory(WindowFactory):
    """
    Конкретная реализация для MacOs
    """
    class Window:
        def __init__(self, name):
            self.name = name
            self.button = []
            self.style = 'Mac Os window style'
        def add_button(self, btn):
            self.button.append(btn.name)
        def show(self):
            print( '{} - {} and {}'.format(self.name, self.style, self.button))
    class Button:
        def __init__(self, name):
            self.name = name
            self.style = 'Mac Os button style'


class LinuxFactory(WindowFactory):
    """
    Конкретная реализация для Linux
    """
    class Window:
        def __init__(self, name):
            self.name = name
            self.button = []
            self.style = 'Ubuntu window style'
        def add_button(self, btn):
            self.button.append(btn.name)
        def show(self):
            print( '{} - {} and {}'.format(self.name, self.style, self.button))
    class Button:
        def __init__(self, name):
            self.name = name
            self.style = 'Ubuntu button style'


def create_dialog(factory):
    """
    функция создания окна при помощи абстрактной фабрики
    """
    wind = factory.create_window('Form1')
    button = factory.create_button('Button1')
    wind.add_button(button)
    return wind

# Допустим мы запустились на Linux
w = create_window(LinuxFactory)
w.show()
# >>> Form1 - Ubuntu window style and ['Button1']