# The max norm that is calculated as the maximum vector values.

# vector max norm
from numpy import inf
from numpy import array
from numpy.linalg import norm

# define vector
a = array([1, 2, 3])
print(a)

# calculate norm
maxnorm = norm(a, inf)
print(maxnorm)

# The length of a vector can be calculated using the maximum norm, also called max norm. Max
# norm of a vector is referred to as Linf where inf is a superscript and can be represented with
# the infinity symbol. The notation for max norm is ||v||inf , where inf is a subscript.

# The max norm is calculated as returning the maximum absolute value of the vector, hence the name.
