# coding: utf-8
# license: GPLv3
from solar_colors import COLORS
from random import choice


class Star:
    """Тип данных, описывающий звезду.
    Содержит массу, координаты, скорость звезды,
    а также визуальный радиус звезды в пикселах и её цвет.
    """

    def __init__(self):
        """
        Constructor of class Star
        """
        self.type = "star"  # Признак объекта звезды
        self.m = 0  # Масса звезды
        self.x = 0  # Координата по оси **x**
        self.y = 0  # Координата по оси **y**
        self.Vx = 0  # Скорость по оси **x**
        self.Vy = 0  # Скорость по оси **y**
        self.Fx = 0  # Сила по оси **x**
        self.Fy = 0  # Сила по оси **y**
        self.R = 5  # Радиус звезды
        self.color = choice(COLORS)  # Цвет звезды
        self.image = None  # Изображение звезды


class Planet:
    """Тип данных, описывающий планету.
    Содержит массу, координаты, скорость планеты,
    а также визуальный радиус планеты в пикселах и её цвет
    """

    def __init__(self):
        """
        Constructor of class Planet
        """
        self.type = "planet"  # Признак объекта планеты
        self.m = 0  # Масса планеты
        self.x = 0  # Координата по оси **x**
        self.y = 0  # Координата по оси **y**
        self.Vx = 0  # Скорость по оси **x**
        self.Vy = 0  # Скорость по оси **y**
        self.Fx = 0  # Сила по оси **x**
        self.Fy = 0  # Сила по оси **y**
        self.R = 5  # Радиус планеты
        self.color = choice(COLORS)  # Цвет планеты
        self.image = None  # Изображение планеты
