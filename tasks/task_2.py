#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from body_package.body import Ball, Parallelepiped

if __name__ == "__main__":
    print("=" * 60)
    print("ДЕМОНСТРАЦИЯ ВСЕХ ПЕРЕОПРЕДЕЛЕННЫХ АБСТРАКТНЫХ МЕТОДОВ")
    print("=" * 60)

    print("\n1. СОЗДАНИЕ ОБЪЕКТОВ НАПРЯМУЮ:")
    print("-" * 40)

    print("\n--- Параллелепипед (прямое создание) ---")
    p1 = Parallelepiped(5, 3, 2)
    print(f"Создан: {p1}")

    print("\n--- Шар (прямое создание) ---")
    b1 = Ball(4)
    print(f"Создан: {b1}")

    print("\n\n2. СОЗДАНИЕ ОБЪЕКТОВ ЧЕРЕЗ from_input():")
    print("-" * 40)

    print("\n--- Создание параллелепипеда через ввод ---")

    import io
    import sys

    test_inputs = ["5", "3", "2"]
    original_stdin = sys.stdin
    sys.stdin = io.StringIO("\n".join(test_inputs))

    p2 = Parallelepiped.from_input()
    print(f"Создан через from_input(): {p2}")

    print("\n--- Создание шара через ввод ---")
    test_inputs = ["4"]
    sys.stdin = io.StringIO("\n".join(test_inputs))

    b2 = Ball.from_input()
    print(f"Создан через from_input(): {b2}")

    sys.stdin = original_stdin

    print("\n\n3. ВЫЗОВ АБСТРАКТНЫХ МЕТОДОВ:")
    print("-" * 40)

    print("\n--- Методы параллелепипеда ---")
    print(f"surface_area(): {p1.surface_area():.2f}")
    print(f"volume(): {p1.volume():.2f}")
    print(f"__str__(): {p1}")

    print("\n--- Методы шара ---")
    print(f"surface_area(): {b1.surface_area():.2f}")
    print(f"volume(): {b1.volume():.2f}")
    print(f"__str__(): {b1}")

    print("\n\n4. ВИРТУАЛЬНЫЕ МЕТОДЫ:")
    print("-" * 40)

    print("\n--- virtual_output() параллелепипеда ---")
    p1.virtual_output()

    print("\n--- virtual_output() шара ---")
    b1.virtual_output()

    print("\n\n5. РАБОТА ЧЕРЕЗ БАЗОВЫЙ КЛАСС Body:")
    print("-" * 40)

    bodies = [p1, b1]

    for i, body in enumerate(bodies, 1):
        print(f"\n--- Тело #{i} ---")
        print(f"Тип: {type(body).__name__}")
        print(f"Площадь поверхности: {body.surface_area():.2f}")
        print(f"Объем: {body.volume():.2f}")
        body.virtual_output()

    print("\n\n6. РАБОТА СО СВОЙСТВАМИ:")
    print("-" * 40)

    print("\n--- Свойства параллелепипеда ---")
    print(f"Длина: {p1.length}")
    print(f"Ширина: {p1.width}")
    print(f"Высота: {p1.height}")

    p1.length = 6
    p1.width = 4
    p1.height = 3
    print(f"После изменения: Длина={p1.length}, Ширина={p1.width}, Высота={p1.height}")
    print(f"Новая площадь поверхности: {p1.surface_area():.2f}")
    print(f"Новый объем: {p1.volume():.2f}")

    print("\n--- Свойства шара ---")
    print(f"Радиус: {b1.radius}")

    b1.radius = 5
    print(f"После изменения: Радиус={b1.radius}")
    print(f"Новая площадь поверхности: {b1.surface_area():.2f}")
    print(f"Новый объем: {b1.volume():.2f}")

    print("\n\n7. ОБРАБОТКА ОШИБОК:")
    print("-" * 40)

    print("\n--- Попытка установки отрицательных значений ---")

    try:
        p1.length = -1
    except ValueError as e:
        print(f"Ошибка параллелепипеда: {e}")

    print("Попытка установки отрицательного радиуса:")
    b1.radius = -1

    print("\n" + "=" * 60)
    print("ДЕМОНСТРАЦИЯ ЗАВЕРШЕНА")
    print("=" * 60)
