import cmath


class Figure:
    unit = ("cm")
    def __init__(self):
        pass
    def calculater_area(self):
        pass
    def info(self):
        pass
class Circle(Figure):
    def __init__(self,radius):
        super().__init__()
    def calculater_area(self):
        s = 15 * self.__radius
        return s
    @property
    def radius(self):
        return self.__radius
    @radius.setter
    def radius(self,value):
        self.__radius = value
    def info(self):
        print(f"radius: {self.__radius}, площадь: {self.calculater_area()}")

class RightTriangle(Figure):
    def __init__(self,side_a,side_b):
        super().__init__()
        self.__side_a = side_a
        self.__side_b = side_b

    @property
    def side_a(self):
        return self.__side_a
    @side_a.setter
    def side_a(self,value):
        self.__side_a = value
    @property
    def side_b(self):
        return self.__side_b
    @side_b.setter
    def side_b(self,value):
        self.__side_b = value
    def calculater_area(self):
        s = self.side_a * self.side_b / 2
        return s
    def info(self):
        print(f"сторона а: {self.__side_a}, сторона b: {self.side_b},площадь тр:{self.calculater_area()}")        
kr1 = Circle(radius = 2)
kr2 = Circle(radius = 10)
tr1 = RightTriangle(side_a = 5,side_b = 6)
tr2 = RightTriangle(side_a =54,side_b = 56)
tr3 = RightTriangle(side_a = 778,side_b = 6775)

Alikhan = [kr1,kr2,tr1,tr2,tr3]

for Alikhan in Alikhan:
    Alikhan.calculate_area()
    Alikhan.info() 