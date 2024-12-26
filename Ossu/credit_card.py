import math 

# what is the min fixed payment they would make per month
def creditCardBi(balance, air, upper=None, lower=None):
    # define upper and lower bounds
    if upper == None:
        upper = (balance * ((1 + air/12) ** 12) ) / 12.0
    if lower == None:
        lower = balance / 12.0
    
    # pick the middle most value in the bouds
    payment = (upper + lower) / 2.0
    
    if abs(upper - lower) < 0.005:
        return round(payment, 2)
    
    # using a loop, check if the value chosen can pay off the balance in 12 months
    newBalance = balance

    for month in range(12):
        # do the payment
        upb = newBalance - payment

        # if the payment is too big 
        if month == 10 and upb <= 0:
            # adjust the upper bound
            return creditCardBi(balance, air, payment, lower)
        
        # if the payment is too small
        if month == 11 and upb > 0:
            # adjust the lower bound
            return creditCardBi(balance, air, upper, payment)
        
        # update the balance
        newBalance = upb + ((air/12) * upb)

    return round(payment,2)
    
    

def creditCardBi2(balance, annualInterestRate):

    monthlyInterestRate = annualInterestRate / 12.0
    lowerBound = balance / 12
    upperBound =  (balance * ((1 + monthlyInterestRate) **12) ) / 12

    while True:
        middleBound = (lowerBound + upperBound) / 2
        unpaidBalance = balance #monthly balance
        for month in range(12):
            newUnpaidBalance = unpaidBalance - middleBound # payment
            unpaidBalance = newUnpaidBalance + (newUnpaidBalance * monthlyInterestRate)
        if abs(unpaidBalance) < 0.005:
            print ("Lowest Payment: {0:.2f}".format(middleBound))
            break

        elif unpaidBalance > 0 : lowerBound = middleBound
        elif unpaidBalance < 0 : upperBound = middleBound



#test regular iteration
if __name__ == "__main__":
    print("Mine Lowest Payment: ", creditCardBi(320000, 0.2))
    print("Them, Lowest: ", creditCardBi2(320000, 0.2))



    def creditCard(balance, air):

        # get the min payment
        result = math.ceil(balance * air/12) + 10
        m_payment = math.ceil(result / 10) * 10

        months = 1
        newBalance = balance


        while months < 13:
            # make the payment
            upb = newBalance - m_payment

            # if unpaid balance <= zero, it's a success
            if upb <= 0: 
                return m_payment
            
            # if we reach month 12 reset and add a multiple of 10
            if months == 12 and upb > 0:

                months = 1
                
                newBalance = balance

                m_payment += 10

                continue


            # figure out the balance for the next month
            newBalance = upb + (air/12 * upb)

            months +=1
