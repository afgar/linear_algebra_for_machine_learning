# The L1 norm that is calculated as the sum of the absolute values of the vector.

# vector L1 norm
from numpy import array
from numpy.linalg import norm

# define vector
a = array([1, 2, 3])
print(a)

# calculate norm
l1 = norm(a, 1)
print(l1)

# The length of a vector can be calculated using the L1 norm, where the 1 is a superscript of
# the L. The notation for the L1 norm of a vector is ||v||1 , where 1 is a subscript. As such, this
# length is sometimes called the taxicab norm or the Manhattan norm.

# The L1 norm is calculated as the sum of the absolute vector values, where the absolute value
# of a scalar uses the notation |a1|. In effect, the norm is a calculation of the Manhattan distance
# from the origin of the vector space.
