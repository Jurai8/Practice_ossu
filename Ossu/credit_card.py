def creditCard(month, balance, air, mrp):
    if month == 0:
        return balance
    else:
        minPay = (balance * mrp) 

        upb = (balance - minPay)

        interest = air/12.0 * upb

        nxtBalance = upb + interest

        return creditCard(month - 1, nxtBalance, air, mrp)
    


if __name__ == "__main__":
    print("remaining balance:", round(creditCard(12, 484, 0.2, 0.04),2))