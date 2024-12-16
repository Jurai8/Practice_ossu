import math

def polysum(n, s):
    # n = number of sides
    # s = length of sides

    area = (0.25*n*s**2) / math.tan(math.pi/n)

    sqPerimeter = (s*n)**2

    polysum = round(area + sqPerimeter, 4)

    return polysum

 
    


if __name__ == "__main__":
    print(polysum(5, 30))