from line import *
import sympy as sp

class Plane:
    def __init__(self, point, normal):
        """ A point on the plane, and normal vector"""
        self.point = point if isinstance(point, Vector3d) else Vector3d(*point)
        self.normal = normal if isinstance(normal, Line3d) else Line3d((0, 0, 0), normal)
        self.d = sum(self.normal.direction ** self.point)

    @classmethod
    def from_3points(cls, point1, point2, point3):
        point1 = point1 if isinstance(point1, Vector3d) else Vector3d(*point1)
        point2 = point2 if isinstance(point2, Vector3d) else Vector3d(*point2)
        point3 = point3 if isinstance(point3, Vector3d) else Vector3d(*point3)

        normal = (point2 - point1).cross(point3 - point1)
        return cls(point1, normal)

    @classmethod
    def from_equation(cls, a, b, c, d):
        """ ax + by + cz = d"""
        return cls((0, 0, d/c), (a, b, c))


    def __add__(self, other):
        """ Check diagonal"""
        if isinstance(other, Plane):
            return self.normal // other.normal
        elif isinstance(other, Line3d):
            return self.normal // other
        return NotImplemented

    def __floordiv__(self, other):
        """ Check parallel"""
        if isinstance(other, Plane):
            return self.normal // other.normal
        elif isinstance(other, Line3d):
            return self.normal + other
        return NotImplemented

    def __sub__(self, other):
        """ Distance between """
        if isinstance(other, (Vector3d, Vector2d)):
            return abs(self.normal.direction * other - self.d) / abs(self.normal.direction)
        elif isinstance(other, Line3d):
            if not self // other: return 0
            else: return self - other.point
        elif isinstance(other, Plane):
            if not self // other: return 0
            else: return abs(self.d - other.d * self.normal.direction.x / other.normal.direction.x) / abs(self.normal.direction)
        else: return NotImplemented

    def __and__(self, other):
        """ Intersection """
        if isinstance(other, Plane):
            if self.normal // other.normal: return 0
            a1, b1, c1, d1 = *self.normal.direction, self.d
            a2, b2, c2, d2 = *other.normal.direction, other.d

            x, y, z = sp.symbols(("x","y","z"))
            eqns = [a1*x+b1*y+c1*z-d1, a2*x+b2*y+c2*z-d2]
            solutions, = sp.linsolve(eqns, [x,y,z])
            point = Vector3d()
            direction = self.normal.direction.cross(other.normal.direction)
            
            x, y, z = 0, 0, 0
            for i, solution in enumerate(solutions):
                point[i] = eval(str(solution))

            return Line3d(point, direction)

        elif isinstance(other, (Vector3d, Vector2d)):
            return not other * self.normal.direction - self.d

        elif isinstance(other, Line3d):
            if self // other:
                if not self - other: return other
                else: return 0
            else:
                t = (self.d - other.point * self.normal.direction) / (other.direction * self.normal.direction)
                return other.point + t * other.direction

        else: return NotImplemented
    

    def __radd__(self, other):
        return self + other

    def __rfloordiv__(self, other):
        return self // other

    def __rsub__(self, other):
        return self - other

    def __repr__(self):
        return f"Plane: {self.normal.direction.x:.2f}x + {self.normal.direction.y:.2f}y + {self.normal.direction.z:.2f}z = {self.d} "

    def __rand__(self, other):
        return self & other


if __name__ == "__main__":
    pass
    
