# Implement the BankAccount class appropriately

class BankAccount:
    def __init__(self, name, account_number, email, balance):
        self.name = name
        self.__account_number = account_number
        self.__email = email
        self.__balance = balance

    def get_account_number(self):
        return self.__account_number
    
    def set_account_number(self, new_account_number):
        self.__account_number = new_account_number

    def get_email(self):
        return self.__email
    
    def set_email(self, new_email):
        self.__email = new_email

    def get_balance(self):
        return self.__balance

    def set_balance(self, new_balance):
        if new_balance < 0 :
            return "The balance cannot be negative"
        else:
            self.__balance = new_balance
    


# Do not change any code below.
# Do not call this function anywhere.
def main():
    name = input()
    account_number = input()
    email = input()
    balance = int(input())
    new_account_number = input()
    new_email = input()
    new_balance = int(input())
    
    account = BankAccount(name, account_number, email, balance)
    
    account.set_email(new_email)
    print(account.get_email())
    
    account.set_account_number(new_account_number)
    print(account.get_account_number())
    
    error_message = account.set_balance(new_balance)
    if error_message:
        print(error_message)
    else:
        print(account.get_balance())

main()
