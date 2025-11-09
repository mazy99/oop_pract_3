#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from tasks.liquid import Alcohol, Liquid

if __name__ == "__main__":
    water = Liquid("Вода", 997)
    print(water)

    water.name = "Дистиллированная вода"
    water.density = 1000
    print(f"После изменений: {water}")
    print(f"Название: {water.name}, Плотность: {water.density}")

    print("\n" + "=" * 50 + "\n")

    vodka = Alcohol("Водка", 940, 40)
    print(vodka)

    vodka.name = "Премиальная водка"
    vodka.density = 942
    vodka.strength = 45
    print(f"После переназначения: {vodka}")

    vodka.strength = vodka.strength - 5
    print(f"После уменьшения крепости: {vodka}")

    print(f"Крепость напитка: {vodka.strength}%")

    try:
        vodka.strength = 150
    except ValueError as e:
        print(f"Ошибка: {e}")

    try:
        water.density = -10
    except ValueError as e:
        print(f"Ошибка: {e}")
