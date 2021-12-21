import math
  
def maxArea (a , b , c , d ):
  
    # Calculating the semi-perimeter
    # of the given quadrilateral
    semiperimeter = (a + b + c + d) / 2
      
    # Applying Brahmagupta's formula to
    # get maximum area of quadrilateral
    return math.sqrt((semiperimeter - a) *
                    (semiperimeter - b) *
                    (semiperimeter - c) * 
                    (semiperimeter - d))

a, b, c, d = map(int,input().split())
print(maxArea(a,b,c,d))
