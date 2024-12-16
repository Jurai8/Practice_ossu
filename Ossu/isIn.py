import math

def isIn(char, aStr):
    
    if (len(aStr) == 1 and char != aStr[0]):
        return False
    
    # start at the middle of the string
    middle = math.floor(len(aStr) / 2)

    if (aStr[middle] == char):
        return True
    elif (aStr[middle] < char):
       # return the first half, exluding the middle char
        return isIn(char, aStr[middle:])
    else:
        # return the second half excluding the middle char
        return isIn(char, aStr[:middle])
 
    


if __name__ == "__main__":
    print(isIn('e', 'fghijkl'))