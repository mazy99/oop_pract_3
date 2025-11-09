#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import math
from abc import ABC, abstractmethod


class Body(ABC):

    @abstractmethod
    def surface_area(self) -> float:
        pass

    @abstractmethod
    def volume(self) -> float:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

    @classmethod
    @abstractmethod
    def from_input(cls) -> "Body":
        pass

    def virtual_output(self) -> None:
        print(f"Площадь поверхности: {self.surface_area():.2f}")
        print(f"Объем: {self.volume():.2f}")


class Parallelepiped(Body):

    def __init__(self, length: float = 0, width: float = 0, height: float = 0):
        self.__length = length
        self.__width = width
        self.__height = height

    @property
    def length(self) -> float:
        return self.__length

    @property
    def width(self) -> float:
        return self.__width

    @property
    def height(self) -> float:
        return self.__height

    @length.setter
    def length(self, new_length: float) -> None:
        if new_length <= 0:
            raise ValueError("Длина должна быть положительной")
        self.__length = new_length

    @height.setter
    def height(self, new_height: float) -> None:
        if new_height <= 0:
            raise ValueError("Высота должна быть положительной")
        self.__height = new_height

    @width.setter
    def width(self, new_width: float) -> None:
        if new_width <= 0:
            raise ValueError("Ширина должна быть положительной")
        self.__width = new_width

    def surface_area(self) -> float:
        return 2 * (
            self.__length * self.__width
            + self.__length * self.__height
            + self.__width * self.__height
        )

    def volume(self) -> float:
        return self.__length * self.__width * self.__height

    def __str__(self) -> str:
        return (
            f"Параллелепипед:\n"
            f"  Длина: {self.__length}\n"
            f"  Ширина: {self.__width}\n"
            f"  Высота: {self.__height}\n"
            f"  Площадь поверхности: {self.surface_area():.2f}\n"
            f"  Объем: {self.volume():.2f}"
        )

    @classmethod
    def from_input(cls) -> "Parallelepiped":
        try:
            length = float(input("Введите длину параллелепипеда: "))
            width = float(input("Введите ширину параллелепипеда: "))
            height = float(input("Введите высоту параллелепипеда: "))
            return cls(length, width, height)
        except ValueError:
            print("Ошибка: введите числовые значения!")
            return cls()

    def virtual_output(self) -> None:
        print(f"Площадь поверхности параллелепипеда: {self.surface_area():.2f}")
        print(f"Объем параллелепипеда: {self.volume():.2f}")


class Ball(Body):

    def __init__(self, radius: float = 0):
        self.__radius = radius

    @property
    def radius(self) -> float:
        return self.__radius

    @radius.setter
    def radius(self, new_radius: float) -> None:
        if new_radius >= 0:
            self.__radius = new_radius
        else:
            print("Ошибка: радиус не может быть отрицательным!")

    def surface_area(self) -> float:
        return 4 * math.pi * self.__radius**2

    def volume(self) -> float:
        return (4 / 3) * math.pi * self.__radius**3

    def __str__(self) -> str:
        return (
            f"Шар:\n"
            f"  Радиус: {self.__radius}\n"
            f"  Площадь поверхности: {self.surface_area():.2f}\n"
            f"  Объем: {self.volume():.2f}"
        )

    @classmethod
    def from_input(cls) -> "Ball":
        try:
            radius = float(input("Введите радиус шара: "))

            if radius < 0:
                print(
                    "Ошибка: радиус не может быть отрицательным! Установлен радиус 0."
                )
                return cls(0)

            return cls(radius)
        except ValueError:
            print("Ошибка: введите числовое значение! Установлен радиус 0.")
            return cls(0)

    def virtual_output(self) -> None:
        print("  Шар:")
        print(f"  Радиус: {self.__radius}")
        print(f"  Площадь поверхности: {self.surface_area():.2f}")
        print(f"  Объем: {self.volume():.2f}")
