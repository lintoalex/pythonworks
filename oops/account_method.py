class bank:
    def create_account(self,acno,ac_type):

        self.bank_name="SBT"

        self.__balance=2000

        self.acno=acno

        self.ac_type=ac_type

    def deposit(self,amount):

        self.__balance+=amount

        print(f"your{self.bank_name} a/c with {self.acno} has been credit{amount} avl balance{self.__balance}")

    def withdraw(self,amount):

        if amount>self.__balance:

            print("transaction faild insufficient balance")

        else:

            self.__balance-=amount

            print(f"your{self.bank_name} a/c with {self.acno} has been debit{amount} avl balance{self.__balance}")

    def get_balance(self):

        print(f"avl balance={self.__balance}")

# user_account=bank()

# user_account.create_account(26453897546,"saving")

# user_account.withdraw(1000)

# user_account.deposit(5000)

vishnu_account=bank()

vishnu_account.create_account(32554775,"saving")

vishnu_account.deposit(5000)

vishnu_account.balance+=20000

