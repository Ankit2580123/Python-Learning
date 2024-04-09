#inmplementation of abstraction
# class Car:
#                     def __init__(self):
#                                         self.acc=False
#                                         self.brake=False
#                                         self.clutch=False
#                     def start(self):
#                                         self.acc=True
#                                         self.brake=True
#                                         self.clutch=True
#                                         print("car started..")
# C = Car()
# C.start()

class Account:
                    def __init__(self,acc,balance):
                                        self.account_no=acc
                                        self.bank_balance=balance
                    
                    def credit(self,amount):
                                        self.bank_balance+=amount
                                        print("Rs.",amount," is Credited")
                                        print("Total Balance: ",self.bank_balance)
                                        
                                        
                    def debit(self,amount):
                                        if(self.bank_balance>amount):
                                                            self.bank_balance-=amount
                                                            print("Rs.",amount," is Debited")
                                                            print("Total Balance: ",self.bank_balance)
                                        else:
                                                            
                                                            print("Existing Balance: ",self.bank_balance," Sorry! Your account have not enough Balance!")
                                                            
                                        
                                        
                    def total_balance(self):
                                        print("Total Balanace.",self.bank_balance)
                                        
account_no=(input("Enter your account Number:")) 
account=Account(account_no,10000)
choice=input(" Choose Credit for C/c and Debit for D : => (c/d)?")
if choice =="c" or choice=='C' or choice=='credit' or choice=='Credit':
                    credit=int(input("Enter the ammount you want to credit:"))
                    account.credit(credit)
elif choice=='d' or choice=='D' or choice=='Debit' or choice=='debit':
                    debit=int(input("Enter the amount you want to debit:"))
                    account.debit(debit)
else:
                    print("Please enter existing choice either c/d")
                                          


