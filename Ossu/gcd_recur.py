def gcdRecur(a, b):
    if (a > b):
        if b == 0:
            return a
        else:
            return gcdRecur(b, a % b)
    if (a < b):
        if a == 0:
            return b
        else:
            return gcdRecur(a, b % a)
 
    


if __name__ == "__main__":
    print(gcdRecur(462, 1071))