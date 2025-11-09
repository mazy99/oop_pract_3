#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Liquid:

    def __init__(self, names: str, dens: float) -> None:

        self.__name = names
        self.__dens = dens

    def __str__(self) -> str:
        return f"Жидкость: {self.name}, Плотность: {self.density} кг/м³"

    @property
    def name(self) -> str:
        return self.__name

    @property
    def density(self) -> float:
        return self.__dens

    @name.setter
    def name(self, new_name: str) -> None:
        self.__name = new_name

    @density.setter
    def density(self, new_dens: float) -> None:
        if new_dens <= 0:
            raise ValueError("Плотсность должна быть положительным числом")
        self.__dens = new_dens


class Alcohol(Liquid):

    def __init__(self, names: str, dens: float, strength: float) -> None:
        super().__init__(names, dens)
        self.__strength = strength

    def __str__(self):
        return f"Алкоголь: {self.name},\
 Плотность: {self.density} кг/м³, Крепость: {self.strength}%"

    @property
    def strength(self) -> float:
        return self.__strength

    @strength.setter
    def strength(self, new_strength: float):
        if new_strength < 0 or new_strength > 100:
            raise ValueError("Крепость должна быть в диапазоне от 0 до 100%")
        self.__strength = new_strength
