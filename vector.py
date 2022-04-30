import math

class Vector2d:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector2d):
            return Vector2d(self.x + other.x, self.y + other.y)
        elif isinstance(other, Vector3d):
            return Vector3d(self.x + other.x, self.y + other.y, other.z)
        elif isinstance(other, tuple):
            return Vector2d(self.x + other[0], self.y + other[1])
        elif isinstance(other, (float, int)):
            return Vector2d(self.x + other, self.y + other)
        else: raise TypeError(f"Unsupported operation between Vector2 and {type(other).__name__}")

    def __sub__(self, other):
        if isinstance(other, Vector2d):
            return Vector2d(self.x - other.x, self.y - other.y)
        elif isinstance(other, Vector3d):
            return Vector3d(self.x - other.x, self.y - other.y, -other.z)
        elif isinstance(other, tuple):
            return Vector2d(self.x - other[0], self.y - other[1])
        elif isinstance(other, (float, int)):
            return Vector2d(self.x - other, self.y - other)
        else: raise TypeError(f"Unsupported operation between Vector2 and {type(other).__name__}")

    def __mul__(self, other):
        if isinstance(other, (Vector2d, Vector3d)):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, tuple):
            return self.x * other[0] + self.y * other[1]
        elif isinstance(other, (float, int)):
            return Vector2d(self.x * other, self.y * other)   
        else: raise TypeError(f"Unsupported operation between Vector2 and {type(other).__name__}")

    def __pow__(self, other):
        if isinstance(other, Vector2d):
            return Vector2d(self.x * other.x, self.y * other.y)
        elif isinstance(other, Vector3d):
            return Vector3d(self.x * other.x, self.y * other.y, 0)
        elif isinstance(other, tuple):
            return Vector2d(self.x * other[0], self.y * other[1])
        else: raise TypeError(f"Unsupported operation between Vector2 and {type(other).__name__}")

    def __radd__(self, other):
        return self.__add__(other)

    def __rsub__(self, other):
        return -self.__sub__(other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5  

    def __eq__(self, other):
        if isinstance(other, Vector2d):
            return self.x == other.x and self.y == other.y
        elif isinstance(other, Vector3d):
            return self.x == other.x and self.y == other.y and other.z == 0
        return False

    def __neg__(self):
        return Vector2d(-self.x, -self.y)

    def __repr__(self):
        return f"Vector2({self.x:.2f},{self.y:.2f})"

    def dist(self, other):
        if isinstance(other, Vector2d):
            return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5 
        elif isinstance(other, Vector3d):
            return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + other.z ** 2) ** 0.5 
        else: raise TypeError(f"Unsupported operation between Vector2 and {type(other).__name__}")

    def cross(self, other):
        if isinstance(other, Vector3d):
            return Vector3d(self.y * other.z,- self.x * other.z, self.x * other.y - self.y * other.x)
        elif isinstance(other, Vector2d):
            return Vector3d(0, 0, self.x * other.y - self.y * other.x) 
        else: raise TypeError(f"Unsupported operation between Vector2 and {type(other).__name__}") 

    def __len__(self):
        return 2

    def __getitem__(self, key):
        if key == 0: return self.x
        elif key == 1: return self.y
        else: raise KeyError("Key range: [0-1]")

    def __iter__(self):
        return iter((self.x, self.y))

    def __rlshift__(self, other):
        return other >= self.x and other <= self.y

    @classmethod
    def from_angle(cls, angle):
        return cls(math.cos(angle), -math.sin(angle))

class Vector3d:
    def __init__(self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        if isinstance(other, Vector3d):
            return Vector3d(self.x + other.x, self.y + other.y, self.z + other.z)
        if isinstance(other, Vector2d):
            return Vector3d(self.x + other.x, self.y + other.y, self.z)
        elif isinstance(other, tuple):
            if len(other) == 2: return Vector3d(self.x + other[0], self.y + other[1], self.z)
            return Vector3d(self.x + other[0], self.y + other[1], self.z + other[2])
        elif isinstance(other, (float, int)):
            return Vector3d(self.x + other, self.y + other, self.z + other)
        else: raise TypeError(f"Unsupported operation between Vector3 and {type(other).__name__}")

    def __sub__(self, other):
        if isinstance(other, Vector3d):
            return Vector3d(self.x - other.x, self.y - other.y, self.z - other.z)
        if isinstance(other, Vector2d):
            return Vector3d(self.x - other.x, self.y - other.y, self.z)
        elif isinstance(other, tuple):
            if len(other) == 2: return Vector3d(self.x - other[0], self.y - other[1], self.z)
            return Vector3d(self.x - other[0], self.y - other[1], self.z - other[2])
        elif isinstance(other, (float, int)):
            return Vector3d(self.x - other, self.y - other, self.z + other)
        else: return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Vector3d):
            return self.x * other.x + self.y * other.y + self.z * other.z
        if isinstance(other, Vector2d):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, tuple):
            if len(other) == 2: return self.x * other[0] + self.y * other[1]
            return self.x * other[0] + self.y * other[1] + self.z * other[2]
        elif isinstance(other, (float, int)):
            return Vector3d(self.x * other, self.y * other, self.z * other)
        else: raise TypeError(f"Unsupported operation between Vector3 and {type(other).__name__}")

    def __pow__(self, other):
        if isinstance(other, Vector3d):
            return Vector3d(self.x * other.x, self.y * other.y, self.z * other.z)
        elif isinstance(other, Vector2d):
            return Vector3d(self.x * other.x, self.y * other.y, 0)
        elif isinstance(other, tuple):
            if len(other) == 2: return Vector3d(self.x * other[0], self.y * other[1], 0)
            return Vector3d(self.x * other[0], self.y * other[1], self.z * other[2])
        else: raise TypeError(f"Unsupported operation between Vector3 and {type(other).__name__}")

    def __radd__(self, other):
        return self.__add__(other)

    def __rsub__(self, other):
        return -self.__sub__(other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5  

    def __eq__(self, other):
        if isinstance(other, Vector3d):
            return self.x == other.x and self.y == other.y and self.z == other.z
        elif isinstance(other, Vector2d):
            return self.x == other.x and self.y == other.y and self.z == 0
        return False

    def __neg__(self):
        return Vector3d(-self.x, -self.y, -self.z)

    def __repr__(self):
        return f"Vector3d({self.x:.2f},{self.y:.2f},{self.z:.2f})"

    def dist(self, other):
        if isinstance(other, Vector3d):
            return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2) ** 0.5 
        elif isinstance(other, Vector2d):
            return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + self.z ** 2) ** 0.5 
        else: raise TypeError(f"Unsupported operation between Vector3 and {type(other).__name__}")

    def cross(self, other):
        if isinstance(other, Vector3d):
            return Vector3d(self.y * other.z - self.z * other.y, self.z * other.x - self.x * other.z, self.x * other.y - self.y * other.x)
        elif isinstance(other, Vector2d):
            return Vector3d(- self.z * other.y, self.z * other.x, self.x * other.y - self.y * other.x) 
        else: raise TypeError(f"Unsupported operation between Vector3 and {type(other).__name__}") 

    def __len__(self):
        return 3

    def __getitem__(self, key):
        if key == 0: return self.x
        elif key == 1: return self.y
        elif key == 2: return self.z
        else: raise KeyError("Key range: [0-2]")

    def __setitem__(self, key, value):
        if key == 0: self.x = value
        elif key == 1: self.y = value
        elif key == 2: self.z = value
        else: raise KeyError("Key range: [0-2]")

    def __iter__(self):
        return iter((self.x, self.y, self.z))

    @classmethod
    def from_Vector2(cls, vector2):
        return cls(vector2.x, vector2.y, 0)

if __name__ == "__main__":
    pass