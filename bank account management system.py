class account:
    def __init__(self,name, acc_no,balance):
        self.name = name
        self.acc_no = acc_no
        self.trans = 0
        if balance < 0:
            print("invalid balance!!")
        else:
            self.opening_balance = balance
            self.final_balance = balance

    def credit(self,amount):
        if amount<= 0:
            print("please enter a positive number!!")
        else:
            self.final_balance += amount 
            self.trans += amount
            self.transaction_type = "deposited"

    def debit(self,amount):
        if amount > self.opening_balance:
            print("insufficient balance")
        else:
            self.final_balance -= amount
            self.trans += amount
            self.transaction_type = "withdrawn"

    def display(self):
        print("=====================")
        print("   ACCOUNT DETAILS ")
        print("=====================\n")

        print(f"Account Holder: {self.name}")
        print(f"Account Number: {self.acc_no}")
        print(f"Opening Balance: {self.opening_balance}")
        print(f"Transaction: {self.transaction_type}")
        print(f"Amount: {self.trans}")
        print(f"Final Balance:{self.final_balance}")  

name = input("enter your name:")
acc_no = input("enter your account number:")
opening_bal = float(input("enter your balance:"))

acc1 = account(name,acc_no,opening_bal)

choice = input("Do you want to credit or debit (c/d):")
if choice == 'c':
    amount = float(input("enter the amount to credit:"))
    acc1.credit(amount)
elif choice == 'd':
    amount = float(input("enter the amount to debit:"))
    acc1.debit(amount)
else:
    print("invalid choice made!!")

acc1.display()
print("thank you for banking with us!")