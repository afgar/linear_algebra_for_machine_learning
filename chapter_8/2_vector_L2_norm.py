# The L2 norm that is calculated as the square root of the sum of the squared vector values.

# vector L2 norm
from numpy import array
from numpy.linalg import norm

# define vector
a = array([1, 2, 3])
print(a)

# calculate norm
l2 = norm(a)
print(l2)

# The length of a vector can be calculated using the L2 norm, where the 2 is a superscript of the
# L. The notation for the L2 norm of a vector is ||v||2 where 2 is a subscript.

# The L2 norm calculates the distance of the vector coordinate from the origin of the vector
# space. As such, it is also known as the Euclidean norm as it is calculated as the Euclidean
# distance from the origin. The result is a positive distance value. The L2 norm is calculated as
# the square root of the sum of the squared vector values.
