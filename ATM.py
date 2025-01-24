class ATM:
    def __init__(self,name,accountno,balance):
        self.name1= name
        self.accountno= accountno
        self.balance= balance
        
    def balance(self):
        print("available balance",self.balance)

    def withdraw(self,amount):
        if(self.balance<amount or amount>10000):
            print("Insufficient amount")
        else:
            print("withdraw successfull",self.balance-amount)


acc1= ATM('keerthi',6123,10000)
print(acc1.name1)



            
        
        
