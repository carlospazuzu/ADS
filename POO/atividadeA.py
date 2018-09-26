import math

class Circle:
 
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
 
class Rectangle:
 
    def __init__(self, corner, width, height):
        self.corner = corner
        self.w = width
        self.h = height
 
    def get_4_corners(self):
        return [Point(self.corner.x, self.corner.y),
                Point(self.corner.x + self.w, self.corner.y),
                Point(self.corner.x, self.corner.y + self.h),
                Point(self.corner.x + self.w, self.corner.y + self.h)
                ]
 
class Point:
 
    def __init__(self, x, y):
        self.x = x
        self.y = y
 
# 3. Escreva uma função denominada point_in_circle, que tome um Circle e um Point e retorne True, se o ponto estiver dentro ou no limite do círculo.
def point_in_circle(p, c):    
    return math.sqrt((p.x - c.center.x) ** 2 + (p.y - c.center.y) ** 2) <= c.radius
 
# 4. Escreva uma função chamada rect_in_circle, que tome um Circle e um Rectangle e retorne True, se o retângulo estiver totalmente dentro ou no limite do círculo.
def rect_in_circle(r, c):
    p1, p2, p3, p4 = r.get_4_corners()
    return point_in_circle(p1, c) and point_in_circle(p2, c) and point_in_circle(p3, c) and point_in_circle(p4, c)
 
# 5 Escreva uma função denominada rect_circle_overlap, que tome um Circle e um Rectangle e retorne True, se algum dos cantos do retângulo cair dentro do círculo. Ou, em uma versão mais desafiadora, retorne True se alguma parte do retângulo cair dentro do círculo.
def rect_circle_overlap(r, c):
    p1, p2, p3, p4 = r.get_4_corners()
    return point_in_circle(p1, c) or point_in_circle(p2, c) or point_in_circle(p3, c) or point_in_circle(p4, c)
 
def main():
    # 2. Instancie um objeto Circle, que represente um círculo com o centro em 150, 100 e raio 75.
    circ = Circle(Point(150, 100), 75)
    ret = Rectangle(Point(150, 100), 10, 10)

    print("O retangulo esta dentro do circulo" if rect_in_circle(ret, circ) else "O retangulo nao esta dentro do circulo")
    print("Um dos cantos do retangulo esta dentro do circulo" if rect_in_circle(ret, circ) else "O retangulo nao esta dentro do circuo")
  
 
if __name__ == "__main__":
    main()