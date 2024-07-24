import math

#This defines the VolTrap class. The __init__ method is the constructor, 
#initializing the object with areas (E and e) and height (u). Default values are 1.

class VolTrap:
    def __init__(self, E=1, e=1, u=1):
        self._E = E
        self._e = e
        self._u = u

    #Set 
    #These are setter methods, allowing you to change the values of E, e, and u after the object is created.        
    
    def setE(self, E):
        self._E = E
    
    def sete(self, e):
        self._e = e
    
    def setu(self, u):
        self._u = u

    #Get
    #These are getter methods, allowing you to retrieve the values of E, e, and u.    
    
    def getArea1(self):
        return self._E
    
    def getArea2(self):
        return self._e
    
    def getHeight(self):
        return self._u

    #This method calculates the volume of the truncated pyramid using the formula and rounds it to 2 decimal places.
    
    def calcVol(self):
        V = (1/3 * (self._E + math.sqrt(self._E * self._e) + self._e)) * self._u
        return round(V, 2)

    #This method defines how the object should be represented as a string.
    
    def __str__(self):
        return f"Volume: {self.calcVol()} m³"
