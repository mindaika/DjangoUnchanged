import math
from decimal import Decimal, getcontext


class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def __add__(self, other):
        return Vector([x + y for x, y in zip(self.coordinates, other.coordinates)])

    def __sub__(self, other):
        return Vector([x - y for x, y in zip(self.coordinates, other.coordinates)])

    def __mul__(self, c):
        return Vector([c * x for x in self.coordinates])

    def times_scalar(self, c):
        new_coordinates = [Decimal(c)*x for x in self.coordinates]
        return Vector(new_coordinates)

    def __round__(self, n=None):
        round_list = []
        for k in self.coordinates:
            round_list.append(round(k, n))
        return Vector(round_list)

    def magnitude(self):
        coords_squared = [x**2 for x in self.coordinates]
        return math.sqrt(sum(coords_squared))

    def normalized(self):
        try:
            magnitude = self.magnitude()
            return self * (Decimal('1.0')/magnitude)

        except ZeroDivisionError:
            raise Exception('Cannot normalize the zero vector')

    def dot(self, v):
        return sum([x*y for x, y in zip(self.coordinates, v.coordinates)])

    def angle_with(self, v, in_degrees=False):
        try:
            u1 = self.normalized()
            u2 = v.normalized()
            angle_in_rads = math.acos(u1.dot(u2))

            if in_degrees:
                degrees_per_rad = 180. / math.pi
                return angle_in_rads * degrees_per_rad
            else:
                return angle_in_rads

        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception('Cannot compute an angle with the zero vector')
            else:
                raise e

    def parallel(self, v):
        print(self.angle_with(v))
        return self.angle_with(v) == 0

    def orthogonal(self, v):
        return self.dot(v) == 0


print('\nLesson 2 - Section 4')
vector4A = Vector((8.218, -9.341))
vector4B = Vector((-1.129, 2.111))
vector4C = Vector((7.119, 8.215))
vector4D = Vector((-8.223, 0.878))
vector4E = Vector((1.671, -1.012, -0.318))
scalar4 = 7.41

print(round(vector4A + vector4B, 3))
print(round(vector4C - vector4D, 3))
print(round(vector4E * scalar4, 3))

print('\nLesson 2 - Section 6')
vector6A = Vector((-0.221, 7.437))
vector6B = Vector((8.813, -1.331, -6.247))
vector6C = Vector((5.581, -2.136))
vector6D = Vector((1.996, 3.108, -4.554))

print(round(vector6A.magnitude(), 3))
print(round(vector6B.magnitude(), 3))
print(round(vector6C.normalized(), 3))
print(round(vector6D.normalized(), 3))

print('\nLesson 2 - Section 8')
vector8A = (7.887, 4.138)
vector8B = (-8.802, 6.776)
vector8C = (-5.955, -4.904, -1.874)
vector8D = (-4.496, -8.755, 7.103)
vector8E = (3.183, -7.627)
vector8F = (-2.668, 5.319)
vector8G = (7.35, 0.221, 5.188)
vector8H = (2.751, 8.259, 3.985)
vector_test1 = Vector((2, 4))
vector_test2 = Vector((1, 2))

print(vector_test1.orthogonal(vector_test2))
print(vector_test1.parallel(vector_test2))

