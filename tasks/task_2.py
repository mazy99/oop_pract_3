#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from body_package.body import Ball, Parallelepiped

if __name__ == "__main__":

    print("\n1. СОЗДАНИЕ ОБЪЕКТОВ:")
    print("-" * 40)

    print("\n--- Параллелепипед ---")
    p1 = Parallelepiped(5, 3, 2)
    print(p1)

    print("\n--- Шар ---")
    b1 = Ball(4)
    print(b1)

    print("\n\n2. ВЫЗОВ АБСТРАКТНЫХ МЕТОДОВ:")
    print("-" * 40)

    print("\n--- Методы параллелепипеда ---")
    print(f"surface_area(): {p1.surface_area():.2f}")
    print(f"volume(): {p1.volume():.2f}")
    print(f"__str__():\n{p1}")

    print("\n--- Методы шара ---")
    print(f"surface_area(): {b1.surface_area():.2f}")
    print(f"volume(): {b1.volume():.2f}")
    print(f"__str__():\n{b1}")

    print("\n\n3. РАБОТА ЧЕРЕЗ БАЗОВЫЙ КЛАСС Body:")
    print("-" * 40)

    bodies = [p1, b1]

    for i, body in enumerate(bodies, 1):
        print(f"\n--- Тело #{i} ({type(body).__name__}) ---")
        print(f"Площадь поверхности: {body.surface_area():.2f}")
        print(f"Объем: {body.volume():.2f}")

    print("\n\n4. РАБОТА СО СВОЙСТВАМИ:")
    print("-" * 40)

    print("\n--- Свойства параллелепипеда ---")
    print(f"Длина: {p1.length}")
    print(f"Ширина: {p1.width}")
    print(f"Высота: {p1.height}")

    p1.length = 6
    p1.width = 4
    p1.height = 3
    print("\nПосле изменения:")
    print(f"Длина={p1.length}, Ширина={p1.width}, Высота={p1.height}")
    print(f"Новая площадь поверхности: {p1.surface_area():.2f}")
    print(f"Новый объем: {p1.volume():.2f}")

    print("\n--- Свойства шара ---")
    print(f"Радиус: {b1.radius}")

    b1.radius = 5
    print(f"\nПосле изменения: Радиус={b1.radius}")
    print(f"Новая площадь поверхности: {b1.surface_area():.2f}")
    print(f"Новый объем: {b1.volume():.2f}")
