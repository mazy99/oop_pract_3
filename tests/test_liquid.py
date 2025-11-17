#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pytest

from tasks.liquid import Alcohol, Liquid


class TestLiquid:

    def test_create_liquid(self):

        liquid = Liquid("Вода", 1000.0)
        assert liquid.name == "Вода"
        assert liquid.density == 1000.0

    def test_liquid_str(self):

        liquid = Liquid("Масло", 850.5)
        expected = "Жидкость: Масло, Плотность: 850.5 кг/м³"
        assert str(liquid) == expected

    def test_change_name(self):

        liquid = Liquid("Вода", 1000.0)
        liquid.name = "Морская вода"
        assert liquid.name == "Морская вода"

    def test_change_density_valid(self):

        liquid = Liquid("Вода", 1000.0)
        liquid.density = 950.5
        assert liquid.density == 950.5

    def test_change_density_invalid(self):

        liquid = Liquid("Вода", 1000.0)

        with pytest.raises(ValueError):
            liquid.density = 0

        with pytest.raises(ValueError):
            liquid.density = -100.0


class TestAlcohol:

    def test_create_alcohol(self):

        alcohol = Alcohol("Водка", 940.0, 40.0)
        assert alcohol.name == "Водка"
        assert alcohol.density == 940.0
        assert alcohol.strength == 40.0

    def test_alcohol_inheritance(self):

        alcohol = Alcohol("Вино", 990.0, 12.5)
        assert isinstance(alcohol, Liquid)

    def test_alcohol_str(self):

        alcohol = Alcohol("Виски", 920.0, 45.0)
        expected = "Алкоголь: Виски, Плотность: 920.0 кг/м³, Крепость: 45.0%"
        assert str(alcohol) == expected

    def test_change_strength_valid(self):

        alcohol = Alcohol("Пиво", 1010.0, 5.0)

        alcohol.strength = 0
        assert alcohol.strength == 0

        alcohol.strength = 100
        assert alcohol.strength == 100

        alcohol.strength = 50.5
        assert alcohol.strength == 50.5

    def test_change_strength_invalid(self):

        alcohol = Alcohol("Ром", 950.0, 40.0)

        with pytest.raises(ValueError):
            alcohol.strength = -1.0

        with pytest.raises(ValueError):
            alcohol.strength = 101.0

    def test_inherited_properties(self):

        alcohol = Alcohol("Текила", 960.0, 38.0)

        alcohol.name = "Золотая текила"
        assert alcohol.name == "Золотая текила"

        alcohol.density = 955.5
        assert alcohol.density == 955.5


def test_multiple_objects():

    water = Liquid("Вода", 1000.0)
    oil = Liquid("Масло", 850.0)

    vodka = Alcohol("Водка", 940.0, 40.0)
    beer = Alcohol("Пиво", 1010.0, 5.0)

    water.name = "Дистиллированная вода"
    assert water.name == "Дистиллированная вода"
    assert oil.name == "Масло"

    vodka.strength = 45.0
    assert vodka.strength == 45.0
    assert beer.strength == 5.0
