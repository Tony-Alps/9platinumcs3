class BankAccount:
#Setting the class up and creating its objects and methods
    def __init__(self, accountNumber, balance):
        self.__accountNumber= accountNumber
        self.__balance= balance

    def set_AccNum(self):
        Verification=int(input("For verification, we need your old Account Number: "))
        if Verification==self.__accountNumber:
            print("Thank you")
            new_AccNum=int(input("Provide the new Account Nmber: "))
            self.__accountNumber=new_AccNum
            print("Account Number changed successfully")
        else:
            print("Account number is incorrect")
        #The set_AccNum method has a security feature i built. It probably won't work because you can just ask for the AccNum, but banks got them so I put it here.
    
    def set_balance(self, new_balance):
        if new_balance >= 0:
            self.__balance = new_balance
            print("Balance changed successfully!")
        else:
            return ("Error: Balance cannot be negative!")

    def get_AccNum(self):
        return f"Account number: {self.__accountNumber}"


    def get_balance(self):
        return f"Balance: {self.__balance}"

#Self is used because variables are private

#Creating the object to be used and the methods to be used
a1=BankAccount(12345,1000)

