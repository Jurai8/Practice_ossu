def gcdIter(a, b):

   testValue = min(a,b)

   while a % testValue != 0 or b % testValue != 0:
       testValue -= 1

   return testValue
 
    


if __name__ == "__main__":
    print(gcdIter(9, 12))