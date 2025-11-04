class savingAccount:
    def __init__(self,name,balance,pinNum):
        self.name=name
        self.balance=balance
        self.pinNum=pinNum
        # self.active=False
        print("Name of account holder",self.name)
    def checkbalance(self,pin):
        if self.pinNum==pin:
            # if self.active==True:
                print(f"{self.balance}")
            # else:
            #     print("account is inactive")
        else:
            print("check pin number")
    def withdraw(self,pin,withd):
        if self.pinNum==pin:
            if withd<=self.balance:
                self.balance-=withd
                print(f"remaing balance--{self.balance}")
            else:
                print("insufficient balance")
        else:
            print("check pin number")
    def deposite(self,pin,deposite):
        if self.pinNum==pin:
            if deposite > 0:
                self.balance+=deposite
                print(f"after deposited balance{self.balance}")

class bussinessAccount:
    def __init__(self,name,bal,pinnum):
        self.name=name
        self.bal=bal
        self.pinnum=pinnum

bankAccount=savingAccount("sravani",50000,2914)
bankAccount1=bussinessAccount("kirnammy",5000000,1795)
pin=int(input("enter pin:---"))
bankAccount.checkbalance(pin)
withd=int(input("enter withdraw amount here:--"))
bankAccount.withdraw(pin,withd)
deposite=int(input("enter deposite amount here:--"))
bankAccount.deposite(pin,deposite)