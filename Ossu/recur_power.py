def recurPower(base, exp):

    if exp == 1:
        return base
    else:
        return base * recurPower(base, exp - 1)
    

if __name__ == "__main__":
    print(recurPower(3, 3))