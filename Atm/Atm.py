class Atm:

    def __init__(Bank, UserAtm_Card_Number, pin_Number):
        Bank.UserAtm_Card_Number = UserAtm_Card_Number
        Bank.pin_Number = pin_Number
    
    #windraws the cash 
    def CashWithdrawl(Bank):
        print('Cash has been withdrawed')
    
    #BalanceEnquiry
    def BalanceEnquiry(Bank):
        print("Amount remaining is $100")

My_Atm = Atm(1000190, 10072)
My_Atm.BalanceEnquiry()