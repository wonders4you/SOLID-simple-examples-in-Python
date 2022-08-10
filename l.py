# SOLID part 3 SO%L%ID
# 
# L - Liskov substitution principle

# Functions that use pointers or references to base classes must
# be able to use objects of derived classes without knowing it.


class Bird():
    def fly():
        pass
    def walking():
        pass
      

class Eagle(Bird):
    def dive():
        pass

# Seems to be ok, but the penguin and the ostrich don't fly.


class Ostrich(Bird):
        pass

# and what about Common swift (Apus apus)?

# To implement something like this, we would have to consider an ostrich, as 
# a bird that flies but doesn't want to fly.
# This breaks Liskow principle, because inherit class cannot supply all methods of parent class.

# The solution is like this:

class FlightlessBirds():
        pass

class FlyingBirds():
        pass

class Ostrich(FlightlessBirds):
        pass

class Eagle(FlyingBirds):
        pass    



# Another example, this time square, and rectangle ...

class Rectangle():
    """
    a four sided-polygon, having all the internal angles equal to 90 degrees
    """
    def width():
        pass
    def height():
        pass

class Square(Rectangle):
    """
    a flat geometric figure that has four equal sides and four right angles
    """
    def width():
        pass
    def height():
        pass
    
# The above example with such an interface breaks the L rule due to the class definition.
# Square class must make sure that the height is equal to the width, moreover changing one
# value in this class should also adjust the other value.

# It doesn't mean, that a square cannot be inherited from a rectangle, it all depends
# on context. 
# 
# See the following example:


class RectangleForGUI():
    """
    a four sided-polygon, having given width or height, with angles equal to 90 degrees
    """
    def width_or_height():
        pass

class SquareForGUI(RectangleForGUI):
    """
    a four sided-polygon, having width or height (which are equal), with angles equal to 90 degrees
    """
    def width_or_height():
        pass

# This application satisfies Liskow Principle.


    









  

  

  
