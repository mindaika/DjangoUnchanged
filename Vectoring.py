import math
from decimal import Decimal, getcontext



class Vector(object):
    getcontext().prec=3

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
        return Vector([Decimal(c) * x for x in self.coordinates])

    def times_scalar(self, c):
        new_coordinates = [Decimal(c)*x for x in self.coordinates]
        return Vector(new_coordinates)

    def __round__(self, n=None):
        return

    def magnitude(self):
        coords_squared = [x**Decimal('2.0') for x in self.coordinates]
        return Decimal(math.sqrt(sum(coords_squared)))

    def normalized(self):
        try:
            return self * (Decimal('1.0')/self.magnitude())

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
vector4A = Vector(('8.218', '-9.341'))
vector4B = Vector(('-1.129', '2.111'))
vector4C = Vector(('7.119', '8.215'))
vector4D = Vector(('-8.223', '0.878'))
vector4E = Vector(('1.671', '-1.012', '-0.318'))
scalar4 = '7.41'

print(vector4A + vector4B)
print(vector4C - vector4D)
print(vector4E * scalar4)

print('\nLesson 2 - Section 6')
vector6A = Vector(('-0.221', '7.437'))
vector6B = Vector(('8.813', '-1.331', '-6.247'))
vector6C = Vector(('5.581', '-2.136'))
vector6D = Vector(('1.996', '3.108', '-4.554'))

print(vector6A.magnitude())
print(vector6B.magnitude())
print(vector6C.normalized())
print(vector6D.normalized())

print('\nLesson 2 - Section 8')
vector8A = Vector(('7.887', '4.138'))
vector8B = Vector(('-8.802', '6.776'))
vector8C = Vector(('-5.955', '-4.904', '-1.874'))
vector8D = Vector(('-4.496', '-8.755', '7.103'))
vector8E = Vector(('3.183', '-7.627'))
vector8F = Vector(('-2.668', '5.319'))
vector8G = Vector(('7.35', '0.221', '5.188'))
vector8H = Vector(('2.751', '8.259', '3.985'))
vector_test1 = Vector(('2', '4'))
vector_test2 = Vector(('1', '2'))

print(vector_test1.orthogonal(vector_test2))
print(vector_test1.parallel(vector_test2))

