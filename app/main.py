import math

class Vector3:
    def __init__(self, x, y, z):
        # x and y components of a vector
        self.x = x;
        self.y = y;
        self.z = z;

        # Magnitude and direction of vector object.
        # Direction is a radian measure bearing 
        self.magnitude = math.sqrt((x*x) + (y*y) + (z*z));
        self.directionX = math.cos(x / self.magnitude);
        self.directionY = math.cos(y / self.magnitude);
        self.directionZ = math.cos(z / self.magnitude);

    def showDetails(self):
        print("Magnitude:", self.magnitude);
        print("Angle with x-axis:", self.directionX);
        print("Angle with y-axis:", self.directionY);
        print("Angle with z-axis:", self.directionZ);

class VectorOperations:
    # Adds two vectors, a and b
    def addVectors(a, b):
        resX = a.x + b.x;
        resY = a.y + b.y;
        resZ = a.z + b.z;

        resultantVector = Vector3(resX, resY, resZ);
        return resultantVector

   # Subtract two vectors, a and b
    def subtractVectors(a, b):
        resX = a.x - b.x;
        resY = a.y - b.y;
        resZ = a.z - b.z;

        resultantVector = Vector3(resX, resY, resZ);
        return resultantVector 

a = Vector3(10, 12, 15)
b = Vector3(10, 12, 15)

result = VectorOperations.addVectors(a, b)
result.showDetails()