from vector import *


class Line3d:
    """https://math.stackexchange.com/questions/404440/what-is-the-equation-for-a-3d-line"""
    def __init__(self, point, direction):
        self.point = point if isinstance(point, Vector3d) else Vector3d(*point)
        self.direction = direction if isinstance(direction, Vector3d) else Vector3d(*direction)

    @classmethod
    def from_end_point(cls, vector1, vector2):
        if not isinstance(vector1, Vector3d): vector1 = Vector3d(*vector1)
        if not isinstance(vector2, Vector3d): vector2 = Vector3d(*vector2)
        return cls(vector1, vector2 - vector1)

    @classmethod
    def from_parameters(cls, x_p, y_p, z_p):
        return cls((x_p[0],y_p[0],z_p[0]), (x_p[1],y_p[1],z_p[1]))

    def __matmul__(self, other, degree = True):
        """ Angle between"""
        if not isinstance(other, Line3d): return NotImplemented
        if degree: return 180 / math.pi * math.asin(abs(self.direction.cross(other.direction)) / (abs(self.direction) * abs(other.direction)))
        else: return math.asin(abs(self.direction.cross(other.direction)) / (abs(self.direction) * abs(other.direction)))

    def __floordiv__(self, other):
        if not isinstance(other, Line3d): return NotImplemented
        return not abs(self.direction.cross(other.direction))

    def __add__(self, other):
        """ Perpendicularity"""
        if isinstance(other, Line3d): return abs(self @ other - 90) < 0.001
        else: 
            return NotImplemented

    def __sub__(self, other):
        if not isinstance(other, (Vector3d, Vector2d, tuple)): return NotImplemented
        return abs((other - self.point).cross(self.direction)) / abs(self.direction)

    def __and__(self, other):
        """ Intersection"""
        if isinstance(other, (Vector3d, Vector2d, tuple)):
            return not (self - other)
        elif isinstance(other, Line3d):
            return not self // other
        else: 
            return NotImplemented

    def __call__(self, t):
        return self.point + t * self.direction

    def __repr__(self):
        return f"Line3d: (x, y, z) = ({self.point.x}, {self.point.y}, {self.point.z}) + t({self.direction.x}, {self.direction.y}, {self.direction.z})"

class Line2d(Line3d):
    def __init__(self, a, b):
        self.point = Vector3d(0, b, 0)
        self.direction = Vector3d(1, a, 0)

    def __repr__(self):
        return f"Line2d: y = {self.direction.y:.2f}x + {self.point.y:.2f}"

class FiniteLine3d():
    def __init__(self, start, direction, end):
        self.line = Line3d(start, direction)
        self.end = end

    @classmethod
    def from_end_point(cls, vector1, vector2):
        if not isinstance(vector1, Vector3d): vector1 = Vector3d(*vector1)
        if not isinstance(vector2, Vector3d): vector2 = Vector3d(*vector2)
        return cls(vector1, vector2 - vector1, vector2)

    @classmethod
    def from_length(cls, vector1, vector2, length):
        if not isinstance(vector1, Vector3d): vector1 = Vector3d(*vector1)
        if not isinstance(vector2, Vector3d): vector2 = Vector3d(*vector2)
        direction = vector2 - vector1
        return cls(vector1, direction, vector1 + vector1 + direction * length)        




if __name__ == "__main__":
    pass



