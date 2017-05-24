from Vectoring import Vector
from decimal import Decimal

print('{} {}'.format('one', 'two'))

def section13():

    print('\nLesson 2 - Section 13')
    v = Vector([8.462, 7.893, -8.187])
    w = Vector([6.984, -5.975, 4.778])
    print(v.cross_product(w))

    v = Vector([-8.987, -9.838, 5.031])
    w = Vector([-4.268, -1.861, -8.866])
    print(v.area_of_parallelogram_with(w))

    v = Vector([1.5, 9.547, 3.691])
    w = Vector([-6.007, 0.124, 5.772])
    print(v.area_of_parallelogram_with(w) * Decimal(0.5))


def section4():

    print('\nLesson 2 - Section 4')
    vector4A = Vector(['8.218', '-9.341'])
    vector4B = Vector(['-1.129', '2.111'])
    vector4C = Vector(['7.119', '8.215'])
    vector4D = Vector(['-8.223', '0.878'])
    vector4E = Vector(['1.671', '-1.012', '-0.318'])
    scalar4 = '7.41'

    print(vector4A.plus(vector4B))
    print(vector4C.minus(vector4D))
    print(vector4E.times_scalar(scalar4))


def section6():

    print('\nLesson 2 - Section 6')
    vector6A = Vector(['-0.221', '7.437'])
    vector6B = Vector(['8.813', '-1.331', '-6.247'])
    vector6C = Vector(['5.581', '-2.136'])
    vector6D = Vector(['1.996', '3.108', '-4.554'])

    print(vector6A.magnitude())
    print(vector6B.magnitude())
    print(vector6C.normalized())
    print(vector6D.normalized())


def section8():
    print('\nLesson 2 - Section 8')
    vector8A = Vector(['7.887', '4.138'])
    vector8B = Vector(['-8.802', '6.776'])
    print(vector8A.dot(vector8B))

    vector8C = Vector(['-5.955', '-4.904', '-1.874'])
    vector8D = Vector(['-4.496', '-8.755', '7.103'])
    print(vector8C.dot(vector8D))

    vector8E = Vector(['3.183', '-7.627'])
    vector8F = Vector(['-2.668', '5.319'])
    print(vector8E.angle_with(vector8F))

    vector8G = Vector(['7.35', '0.221', '5.188'])
    vector8H = Vector(['2.751', '8.259', '3.985'])
    print(vector8G.angle_with(vector8H, in_degrees=True))

    vector_test1 = Vector(['2', '4'])
    vector_test2 = Vector(['1', '2'])

    # print(vector_test1.orthogonal(vector_test2))
    # print(vector_test1.parallel(vector_test2))

def section10():
    print('\nLesson 2 - Section 10 : Checking for parallelism and orthogonality')
    vector10A = Vector(['-7.579', '-7.88'])
    vector10B = Vector(['22.737', '23.64'])
    vector10C = Vector(['-2.029', '9.97', '4.172'])
    vector10D = Vector(['-9.231', '-6.639', '-7.245'])
    vector10E = Vector(['-2.328', '-7.284', '-1.214'])
    vector10F = Vector(['-1.821', '1.072', '-2.94'])
    vector10G = Vector(['2.118', '4.827'])
    vector10H = Vector(['0', '0'])

    print(vector10A, ' and\n', vector10B, ' are:')
    if (vector10A.is_parallel_to(vector10B)):
        print('parallel\n')

    if (vector10A.is_orthogonal_to(vector10B)):
        print('orthogonal\n')

    print(vector10C, ' and\n', vector10D, ' are:')
    if (vector10C.is_parallel_to(vector10D)):
        print('parallel\n')

    if (vector10C.is_orthogonal_to(vector10D)):
        print('orthogonal\n')

    print(vector10E, ' and\n', vector10F, ' are:')
    if (vector10E.is_parallel_to(vector10F)):
        print('parallel\n')

    if (vector10E.is_orthogonal_to(vector10F)):
        print('orthogonal\n')

    print(vector10G, ' and\n', vector10H, ' are:')
    if (vector10G.is_parallel_to(vector10H)):
        print('parallel\n')

    if (vector10G.is_orthogonal_to(vector10H)):
        print('orthogonal\n')


def section12():
    print('\nLesson 2 - Section 12 : Coding vector projections\n')

    v = Vector([3.039, 1.879])
    b = Vector([0.825, 2.036])
    print('The projection of\n', v, '\nonto\n', b, '\nis\n', v.project_onto(b))

    v = Vector([-9.88, -3.264, -8.159])
    b = Vector([-2.155, -9.353, -9.473])
    print('\nThe perp is: ', v.component_orthogonal_to(b))

    v = Vector([3.009, -6.172, 3.691, -2.51])
    b = Vector([6.404, -9.144, 2.759, 8.718])

    print('\nThe Whatevs is: ', v.component_parallel_to(b), ' + ', v.component_orthogonal_to(b))

#section4()
#section6()
#section8()
#section10()
section12()
#section13()