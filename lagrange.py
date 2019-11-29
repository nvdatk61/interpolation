from sympy import *
from sympy.matrices import *
import numpy
import pylab
import warnings


def Lagrange_interpolation(points, variable=None):
    """
    Compute the Lagrange interpolation polynomial.

    :var points: A numpy n×2 ndarray of the interpolations points
    :var variable: None, float or ndarray
    :returns:   * P the symbolic expression
                * Y the evaluation of the polynomial if `variable` is float or ndarray

    """
    x = Symbol("x")
    L = zeros(1, points.shape[0])
    i = 0

    for p in points:
        numerator = 1
        denominator = 1
        other_points = numpy.delete(points, i, 0)

        for other_p in other_points:
            numerator = numerator * (x - other_p[0])
            denominator = denominator * (p[0] - other_p[0])

        L[i] = numerator / denominator
        i = i + 1

    # The Horner factorization will reduce chances of issues with floats approximations
    P = horner(L.multiply(points[..., 1])[0])
    Y = None

    try:
        Y = lambdify(x, P, 'numpy')
        Y = Y(variable)

    except:
        warnings.warn("No input variable given - polynomial evaluation skipped")

    return P, Y


def test_Lagrange(sets):
    for points in sets:
        x = numpy.linspace(0, 100)
        P, Y = Lagrange_interpolation(points, x)
        print(P)
        pylab.plot(x, Y)


if __name__ == '__main__':
    sets = [numpy.array([  # Linear
        [0, 1],
        [50, 50],
    ]),
        numpy.array([  # Quadratic
            [0, 1],
            [50, 50],
            [100, 1]
        ]),
        numpy.array([  # Cubic
            [0, 1],
            [50, 50],
            [75, 40],
            [100, 1]
        ])
    ]

    test_Lagrange(sets)