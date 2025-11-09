#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import math

import pytest

from tasks.body_package.body import Ball, Body, Parallelepiped


class TestParallelepiped:
    """Тесты для класса Parallelepiped"""

    def test_create_parallelepiped(self):
        """Тест создания параллелепипеда"""
        p = Parallelepiped(2.0, 3.0, 4.0)
        assert p.length == 2.0
        assert p.width == 3.0
        assert p.height == 4.0

    def test_surface_area(self):
        """Тест вычисления площади поверхности"""
        p = Parallelepiped(2.0, 3.0, 4.0)
        expected_area = 2 * (2 * 3 + 2 * 4 + 3 * 4)
        assert p.surface_area() == expected_area

    def test_volume(self):
        """Тест вычисления объема"""
        p = Parallelepiped(2.0, 3.0, 4.0)
        assert p.volume() == 2.0 * 3.0 * 4.0

    def test_setters_valid(self):
        """Тест сеттеров с валидными значениями"""
        p = Parallelepiped(1.0, 1.0, 1.0)
        p.length = 5.0
        p.width = 6.0
        p.height = 7.0
        assert p.length == 5.0
        assert p.width == 6.0
        assert p.height == 7.0

    def test_setters_invalid(self):
        """Тест сеттеров с невалидными значениями"""
        p = Parallelepiped(1.0, 1.0, 1.0)

        with pytest.raises(ValueError):
            p.length = 0

        with pytest.raises(ValueError):
            p.width = -1.0

        with pytest.raises(ValueError):
            p.height = -5.0

    def test_str_representation(self):
        """Тест строкового представления"""
        p = Parallelepiped(2.0, 3.0, 4.0)
        result = str(p)
        assert "Параллелепипед:" in result
        assert "Длина: 2.0" in result
        assert "Ширина: 3.0" in result
        assert "Высота: 4.0" in result


class TestBall:
    """Тесты для класса Ball"""

    def test_create_ball(self):
        """Тест создания шара"""
        ball = Ball(5.0)
        assert ball.radius == 5.0

    def test_surface_area(self):
        """Тест вычисления площади поверхности шара"""
        ball = Ball(3.0)
        expected_area = 4 * math.pi * 3.0**2
        assert ball.surface_area() == expected_area

    def test_volume(self):
        """Тест вычисления объема шара"""
        ball = Ball(3.0)
        expected_volume = (4 / 3) * math.pi * 3.0**3
        assert ball.volume() == expected_volume

    def test_radius_setter_valid(self):
        """Тест сеттера радиуса с валидными значениями"""
        ball = Ball(1.0)
        ball.radius = 10.0
        assert ball.radius == 10.0

        ball.radius = 0.0
        assert ball.radius == 0.0

    def test_radius_setter_invalid(self):
        """Тест сеттера радиуса с невалидными значениями"""
        ball = Ball(5.0)

        ball.radius = -1.0
        assert ball.radius == 5.0

    def test_str_representation(self):
        """Тест строкового представления"""
        ball = Ball(5.0)
        result = str(ball)
        assert "Шар:" in result
        assert "Радиус: 5.0" in result


class TestInheritanceAndAbstract:
    """Тесты наследования и абстрактных методов"""

    def test_inheritance(self):
        """Тест что классы наследуются от Body"""
        p = Parallelepiped(1.0, 1.0, 1.0)
        ball = Ball(1.0)

        assert isinstance(p, Body)
        assert isinstance(ball, Body)

    def test_abstract_methods_implementation(self):
        """Тест что все абстрактные методы реализованы"""
        p = Parallelepiped(1.0, 1.0, 1.0)
        ball = Ball(1.0)

        assert p.surface_area() > 0
        assert p.volume() > 0
        assert isinstance(str(p), str)

        assert ball.surface_area() > 0
        assert ball.volume() > 0
        assert isinstance(str(ball), str)


class TestVirtualMethods:
    """Тесты виртуальных методов"""

    def test_virtual_output(self):
        """Тест метода virtual_output"""
        p = Parallelepiped(2.0, 3.0, 4.0)
        ball = Ball(3.0)

        p.virtual_output()
        ball.virtual_output()


def test_multiple_objects():
    """Тест работы с несколькими объектами"""

    p1 = Parallelepiped(1.0, 2.0, 3.0)
    p2 = Parallelepiped(4.0, 5.0, 6.0)

    ball1 = Ball(2.0)
    ball2 = Ball(4.0)

    assert p1.volume() == 6.0
    assert p2.volume() == 120.0

    assert ball1.volume() == (4 / 3) * math.pi * 8.0
    assert ball2.volume() == (4 / 3) * math.pi * 64.0


def test_edge_cases():
    """Тест граничных случаев"""

    p_small = Parallelepiped(0.1, 0.1, 0.1)
    assert p_small.volume() > 0

    ball_zero = Ball(0.0)
    assert ball_zero.surface_area() == 0.0
    assert ball_zero.volume() == 0.0


def test_calculation_accuracy():
    """Тест точности вычислений"""

    p = Parallelepiped(2, 3, 4)
    assert p.surface_area() == 52.0
    assert p.volume() == 24.0

    ball = Ball(1.0)
    assert abs(ball.surface_area() - 12.56637) < 0.001
    assert abs(ball.volume() - 4.18879) < 0.001
