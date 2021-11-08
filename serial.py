"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    """Initiates serail number class using start value"""
    def __init__ (self,start=0):
        self.start = self.next = start
    """ returns start value with first run, then increments by 1"""
    def generate(self):
        self.next += 1
        return self.next -1
    """resets serial number back to starting value when generat runs again"""
    def reset(self):
        self.next = self.start
    
    def __repr__(self):
        return f"SerialGenerator(start = {self.start}, next = {self.next})"
