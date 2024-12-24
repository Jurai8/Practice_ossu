 # def creditCard(month, balance, air, mrp):
    #if month == 0:
       # return balance
   # else:
     #   minPay = (balance * mrp) 

     #   upb = (balance - minPay)

    #    interest = air/12.0 * upb

     #   nxtBalance = upb + interest

     #   return creditCard(month - 1, nxtBalance, air, mrp)

# what is the min fixed payment they would make per month
def creditCard(balance, air):

    #figure out the fixed payment
    m_payment = 10
    months = 1
    newBalance = balance

    # maybe decide m_payment by the starting value? the interest rate or the starting balance? or the nextmonths balance if nothing were to be paid?

    while months < 13:

        upb = balance - m_payment

        # if unpaid balance = zero, it's a success
        if upb <= 0: 
            
            return
        
        # if we reach month 12 reset and add a multiple of 10
        if months == 12:
            months = 1
            m_payment *= 5
            continue


        # figure out the balance for the next month
        newBalance += upb + (air/12 * upb)

        months +=1
    # if balance is less than or = 0

#test regular iteration
if __name__ == "__main__":
    print("remaining balance:", round(creditCard(12, 3329, 0.2),2))