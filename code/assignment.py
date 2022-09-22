"""
Program Description: Bank Management system

Development Environment: This program was developed in Visual Studio Code.

Author: Habeeb Alao

Created: 06/12/2021    Modified: 16/12/2021
"""

# imporitng self-studied module datetime from "https://docs.python.org/3/library/datetime.html"
from datetime import datetime

# importing random module
import random

# using self-studied module tabulate  from "https://pypi.org/project/tabulate/"
from tabulate import tabulate

# importing os to get path
import os

class Bank:
    """ bank class holds the bank's headquarters information """

    def __init__(self):
        """ initialises the bank's headquarter information """
        self.bankName = "Bank Of H"
        self.Headquarters = "321 Really Rich Road"


class BankBranch(Bank):
    """ bank class has only one method "__init__" """

    def __init__(self, BankName="Bank of H"):
        """ initialises the bank's branch information """
        super().__init__()
        self.bankName = BankName
        self.bankBranchAddress = "123 Wealthy Way"
        self.bankContactEmail = "INFO@BOH.IE"
        self.bankContactNumber = "8923-422-455"


class Customer(BankBranch):
    """ customer class holds customers name and age """

    def __init__(self, name="null", age=0):
        """takes in self, name and age and assigns them to the objects attributes"""
        super().__init__()
        self.name = name
        self.age = age
        self.email = str(name) + "@boh.com"
        self.address = "adresss"

    def __str__(self):
        """takes in self and returns the customers name and age attributes"""
        return "{},{}".format(self.name, self.age)


class Account(Customer):
    """ 
    subclass of customer and inherites all of the customers attributes and methods

    contains several customs methods including myDetails, myTransactions, balance, deposit, withdraw and transfer.
    """

    def __init__(self, name="null", age=0,  accountNumber=0, IBAN=0, PIN=0000, funds=0.00):
        """
        takes in / inherits customers attributes and accountNumber, IBAN, and funds.
        initialises the Account attributes 
        """
        # calling super() function to inherit parent class attributes
        super().__init__(name, age)

        # initializing attributes
        self.IBAN = IBAN
        self.accountNumber = accountNumber
        self.funds = float(funds)
        self.pin = PIN

    def myDetails(self):
        """takes in self and returns the Account attributes details"""
        return "\nYour Bank Details\nAccount Number: {}\nName: {}\nAge: {}\nIBAN: {}\nPIN: {}\nBalance: {}\n".format(self.accountNumber, self.name, self.age, self.IBAN, str(self.pin),self.funds)

    def myTransactions(self):
        """takes in self and returns the Account transactions"""

        if "..." in (str(self.transactions)):
            return "You have no transactions"

        listOflist = []
        # initialises list that will hold list of all transactions for this user
        listOflist = str(self.transactions.replace("['", "").replace(
            "']", "").replace(" (", "").replace("(", "")).split("),")

        copyOf_listOflist = listOflist.copy()

        ARR = []
        for element in copyOf_listOflist:
            ARR.append(element.split(","))

        # prints all transaction is a table format
        # self studied module from "https://pypi.org/project/tabulate/" used to format tables nicely
        return tabulate(ARR, headers=['DATE', 'IN/OUT', 'AMOUNT', 'BALANCE', 'SOURCE'], tablefmt='fancy_grid')

    def balance(self):
        """takes in self and returns the Account funds"""

        return "your balance is {}".format(self.funds)

    def deposit(self, amount, source=0):
        """
        takes in self, amount and source.

        increments account by deposit amount

        and appends the transaction to the transactions list(of tuples).

        returns a success message including amont deposited and the new account balance.
        """

        # checks if deposit amount is a negative number then returns to main if it is after showing a error message
        if amount <= 0:
            print("You can only deposit a positive value")
            return

        # increments the cusotmers funds by the deposit amount
        self.funds += amount

        # if the source of the funds is -  this means it was done by who ever owns the account
        if (source == 0):
            # formats the transaction to have the source of the money to be deposit
            transaction = (datetime.now().strftime("%d-%b-%y"),
                           "IN", amount, self.funds, "deposit")
        # else the deposit was made via transfer by another cusotmer
        else:
            # fomats the customer's transaction to include the source account of the transfer
            transaction = (datetime.now().strftime("%d-%b-%y"), "IN",
                           amount, self.funds, "transfer from "+str(source))

        
        # appends the transaction to the transactions list as a tuple so it cant be changed.
        if "..." in str(self.transactions).replace("['", "").replace("']", "").replace(" (", "").replace("(", "").replace("[", "").replace("]", ""):
            self.transactions = str(transaction)
        else:
            self.transactions = str(self.transactions) + \
                ", {}".format(str(transaction))

        # returns success message
        return "{} has succesfully been deposited new balance is: {}\n".format(amount, self.funds)

    def withdraw(self, amount):
        """
        takes in self, amount.

        decrements account by withdrawal amount.

        and appends the transaction to the transactions list(of tuples).

        returns a success message including amount withdrawed and new balance.
        """

        # checks if deposit amount is a negative number then returns to main if it is after showing a error message
        if amount <= 0:
            print("You can only withdraw a positive value")
            return

        # decrements the cusotmers funds by the withdrawal amount
        self.funds -= amount

        # formats the transaction details
        transaction = (datetime.now().strftime("%d-%b-%y"),
                       "OUT", amount, self.funds, "withdrawal")

        # appends the transaction to the transactions list as a tuple so it cant be changed.
        self.transactions = str(self.transactions) + \
            ", {}".format(str(transaction))

        # return success message to user
        return ("{} has succesfully been withdrawed new balance is: {}\n".format(amount, self.funds))

    def transfer(self, amount=0, account_number=0):
        """
        takes in self and destination account number.

        decrements self.funds and increments desitnation accounts funds by the transfer amount.

        appends transfer transaction to the transactions list(of tuples).

        returns success message.

        """

        # checks if transfer amount is a negative number then returns to main if it is after showing a error message
        if amount <= 0:
            print("You can only send a positive value")
            return

        # decrements the customers account's funds by the trnasfer amount
        self.funds -= amount

        # call the deposit fucntions for the destinations user also passing its self.accountNumber as the source of the money
        Accounts[str(account_number)].deposit(amount, self.accountNumber)

        # formats the transactions details
        transaction = (datetime.now().strftime("%d-%b-%y"),
                       "OUT", amount, self.funds, "transfer")

        # appends the transaction to the transactions list as a tuple so it cant be changed.
        self.transactions = str(self.transactions) + \
            ", {}".format(str(transaction))

        # returns success message
        return print("successfully transfered {} to {}".format(amount, str(account_number)))

    def __str__(self):
        """takes in self and returns all the initialised account attributes accountNumber, IBAN and funds including inherited attributes """
        return super().__str__() + ",{},{},{},{}".format(self.accountNumber, self.IBAN,self.pin, self.funds)


class SavingAccount(Account, Customer):
    """
    Subclass of account class and cusotmer class
    """

    def __init__(self, name="null", age=0,  accountNumber=0, IBAN=0,PIN=0000, funds=0.00, transactions=None, AccountType="SavingAccount"):
        """
        takes in customer and account attributes and account type
        using super() it traverses the MRO and assigns the attributes to the SavingAccount class.
        """
        super().__init__(name, age, accountNumber, IBAN, PIN, funds)

        # if there are no transactions then initialise an empty list
        if transactions is None:
            self.transactions = "..."
        # otherwise initialsie the list and append to the end of the list
        else:
            self.transactions = transactions
            self.transactions.append(transactions)

        # initialise the account type attribute to be "SavingAccount"
        self.AccountType = AccountType

        # initalise the "SavingAccount" class attribute to 0 mening no negative balance allowed
        self.credit_limit = 0

    def transfers(self, amount=0, account_number=0):
        """ 
        takes in self, amount, account_number
        checks if tranfer limit for the month has been exeeded or the transfer exeeds the credit limit
        then inherits and call the transfer method from the account class.
        """
        # initialises list that will hold list of all transactions for this user
        listOflist = []
        

        listOflist = str(self.transactions.replace("['", "").replace(
            "']", "").replace(" (", "").replace("(", "")).split("),")

        copyOf_listOflist = listOflist.copy()

        ARR = []
        for element in copyOf_listOflist:
            ARR.append(element.split(","))

        # determins the length of a month
        month = datetime.strptime(
            "31-Dec-21", '%d-%b-%y') - datetime.strptime("1-Dec-21", '%d-%b-%y')

        time_between_last_out_transaction = month * 2
        loc = -1

        for el in range(0, int(len(self.transactions[0]))):
            if "OUT" in copyOf_listOflist:
                loc = int(el)

        if loc != -1:
            # initialize date object of the last transaction date
            date_1 = ARR[loc][0]
            date_object_1 = datetime.strptime(date_1, '%d-%b-%y')

            # initialize the the current date object
            date_2 = (str(datetime.now().strftime("%d-%b-%y")))
            date_object_2 = datetime.strptime(date_2, '%d-%b-%y')

            #  print((datetime.now().strftime("%b")) > datetime.strptime(date_1, "%b"))

            # find the time since the last (withdraw or transfer) transaction
            time_between_last_out_transaction = date_object_2 - date_object_1

            

            # checks if only one trasaction(out) occured in th last month
            if (month > time_between_last_out_transaction):
                print("{} is the date of your last OUT transaction ".format(
                    self.transactions[0][loc][1:10]))
                return "max transfers for this month has been met"

        # checks if the transfer will exceed the credit limit
        if (self.funds - amount < self.credit_limit):
            print("this trandsfer exeeds your your balance of {}".format(self.funds))
            return

        # calls the inherited transfer method from account
        return super().transfer(amount, account_number)

    def withdraws(self, amount=0):
        """ 
        takes in self and amount
        checks if withdrawal limit for the month has been exeeded or the withdrawal exeeds the credit limit
        then inherits and call the withdraw method from the account class.
        """

        if (self.balance == 0.00):

            # initialises list that will hold list of all transactions for this user
            listOflist = []
            
            listOflist = str(self.transactions.replace("['", "").replace(
                "']", "").replace(" (", "").replace("(", "")).split("),")

            copyOf_listOflist = listOflist.copy()

            ARR = []
            for element in copyOf_listOflist:
                ARR.append(element.split(","))

            # determins the length of a month
            month = datetime.strptime(
                "31-Dec-21", '%d-%b-%y') - datetime.strptime("1-Dec-21", '%d-%b-%y')

            time_between_last_out_transaction = month * 2
            loc = -1

            for el in range(0, int(len(self.transactions[0]))):
                if "OUT" in copyOf_listOflist:
                    loc = int(el)

            if loc != -1:
                # initialize date object of the last transaction date
                date_1 = ARR[loc][0]
                date_object_1 = datetime.strptime(date_1, '%d-%b-%y')

                # initialize the the current date object
                date_2 = (str(datetime.now().strftime("%d-%b-%y")))
                date_object_2 = datetime.strptime(date_2, '%d-%b-%y')

                #  print((datetime.now().strftime("%b")) > datetime.strptime(date_1, "%b"))

                # find the time since the last (withdraw or transfer) transaction
                time_between_last_out_transaction = date_object_2 - date_object_1

                # checks if only one trasaction(out) occured in th last month
                if (month > time_between_last_out_transaction):
                    return "max withdrawals for this month has been met"

        # checks if the withrdrawal will exceed the credit limit
        if (self.funds - amount < self.credit_limit):
            return "this trandsfer exeeds your your balance of {}".format(self.funds)

        # calls the inherited withdraw method from account
        return super().withdraw(amount)

    def __str__(self):
        """ takes in self and returns all the Saving Account attributes including all inherited attributes """
        return super().__str__() + ",{}".format(self.AccountType)


class CheckingAccount(Account, Customer):
    """
    subclass of account and customer
    takes in customer and account attributes and account type
    using super() it traverses the MRO and assigns the attributes to the CheckingAccount class.
    """

    def __init__(self, name="null", age=0,  accountNumber=0, IBAN=0, PIN=0000,funds=0.00, transactions=None, AccountType="CheckingAccount"):
        super().__init__(name, age, accountNumber, IBAN, PIN, funds)

        # initialises the cheking account credit limit ot -500
        self.credit_limit = -500

        # if there are no transactions then initialise an empty list
        if transactions is None:

            self.transactions = "..."
        # otherwise initialsie the list and append to the end of the list
        else:
            self.transactions = transactions
            self.transactions.append(transactions)

        # initialise the account type attribute to be "CheckingAccount"
        self.AccountType = AccountType

    def transferc(self, amount=0, account_number=0):
        """
        takes in self, amount, account_number.
        checks if the transfer will exeed the credit limit of the customers account
        then calls the inherited account transfer method 
        """

        # checks if the transfer will exceed the credit limit
        if (self.funds - amount < self.credit_limit):
            print("this trandsfer exeeds your credit limit of {}".format(
                self.credit_limit))
            return

        # calls the inherited transfer method from account
        return super().transfer(amount, account_number)

    def withdrawc(self, amount):
        """
        takes in self, amount
        checks if the withdrawal will exeed the credit limit of the customers account
        then calls the inherited account withdraw method 
        """

        # checks if the withdrawla will exceed the credit limit
        if (self.funds - amount < self.credit_limit):
            print("this trandsfer exeeds your credit limit of {}".format(
                self.credit_limit))
            return

        # calls the inherited withdraw method from account
        return super().withdraw(amount)

    def __str__(self):
        """ takes in self and returns all the Saving Account attributes including all inherited attributes """
        return super().__str__() + ",{}".format(self.AccountType)

# function that outputs the main menu for the user


def MainMenu():
    print("\n")
    print("||           ----- Main Menu -----       ||")
    print("|| 1. Create A New Account               ||")
    print("|| 2. view your transactions             ||")
    print("|| 3. Customer operations                ||")
    print("|| 4. Customer deletes his/her account.  ||")
    print("|| 5. exit                               ||")

# function that outputs the method operattions menu for the user


def MethodMenu():
    print("\n")
    print("||       ----- Method Op Menu -----      ||")
    print("|| 1. See your account details           ||")
    print("|| 2. Deposit money                      ||")
    print("|| 3. Witdraw money                      ||")
    print("|| 4. See Balance                        ||")
    print("|| 5. Transfer money to another account  ||")
    print("|| 6. return to main menu                ||")

# function that updates "Accounts.txt"


def UpdateAccounts():
    filehandle = open("code/Accounts.txt", "w") 
    for key in Accounts:
        packed_str = str(key) + ":" + str(Accounts[key]).replace("\'", "").replace(
            "[, ", "[").replace("]", "").replace("[", "").replace("((", "(") + "\n"
        filehandle.writelines(packed_str)
    filehandle.close()

# function that updates "Customers.txt"


def UpdateCustomers():
    filehandle2 = open("code/Customers.txt", "w")
    for key in Customers:
        packed_str = str(key) + ":" + str(Customers[key]).replace("\'", "").replace(
            "[, ", "[").replace("]", "").replace("[", "").replace("((", "(") + "\n"
        filehandle2.writelines(packed_str)
    filehandle2.close()

# function that updates "AccountsTrasactions.txt"


def UpdateAccountsTransaction():
    filehandle = open("code/AccountsTransactions.txt", "w")
    for key in Accounts:
        packed_str = str(key) + ":" + str(Accounts[key].transactions).replace("[[", "").replace("]", "").replace(
            "[", "").replace("]]", "").replace("\'", "").replace("\\", "").replace("n]", "").replace(")n", ")").replace("\n", "") + "\n"
        filehandle.writelines(packed_str)
    filehandle.close()

# function that unpacks the file thats stores customer account details


def unpackFiles():
    a_file = open("code/Accounts.txt")
    

    for line in a_file:

        key, value = line.split(":")

        value_list = value.replace(" ", "").split(",")

        if "SavingAccount" in value_list[(len(value_list))-1]:
            Accounts[key] = SavingAccount(
                value_list[0], value_list[1], value_list[2], value_list[3], value_list[4],value_list[5], [])
        else:
            Accounts[key] = CheckingAccount(
                value_list[0], value_list[1], value_list[2], value_list[3], value_list[4], value_list[5], [])

        Customers[value_list[0]] = Customer(value_list[0], value_list[1])
    a_file.close()

    b_file = open("code/AccountsTransactions.txt")

    for line in b_file:

        key, value = line.split(":")

        if str(value).count(")") == 1:
            # one transaction
            Accounts[key].transactions = (str(value.replace(":(", ":").replace(
                "\n", "").replace("[", "[").replace("]]", "").replace("\'", "").replace("\n", "")))

        elif value.count("),") > 0:
            # if multiple transactions

            Accounts[key].transactions = (str(value.replace(":(", ":").replace("\n", "").replace(
                "[", "[").replace("]]", "").replace("\'", "").replace("\n", "").split("),(")))

    b_file.close()


# initialise dictionaries
Accounts = {}
Customers = {}

# calls to unpack files
unpackFiles()


# keeps returning mainmenu until user exits by selecting the exit option
while True:
    # makes sure all files are updated
    UpdateAccounts()
    UpdateCustomers()
    UpdateAccountsTransaction()
    unpackFiles()

    # calls main menu function to display main menu
    MainMenu()

    # prompts user to input a menu option
    userAnswer = input("|| --> Enter your choice: ")

    # try exept block for error checking validation if input doesnt match wante input
    try:
        # converts the inputed option string to a float
        option = float(userAnswer)

        # if user selctions option 1 from main menu
        if option == 1:
            print('Create A New Account \'Option 1\'\n')

            # prompt user to input thei name and age
            name = input("Please enter your full name: ")
            age_ = input("Please enter your age: ")
            # email =  input("please enter your email address")
            # address = input("please enter your address")
            age = int(age_)

            while True:

                # validates user enters number
                try:

                    # if user is of age to make either a checking or saving account
                    if (age >= 18):
                        print("what type of account would you like to open?")
                        print("savings or cheking")

                        # prompt user to select account type
                        accountSelect = float(
                            input("|| 1. SavingAccount | 2. CheckingAccount\n-> "))
                    # if user is old enough to make only a cheking account
                    elif((13 < age) and (age < 18)):
                        print(
                            "only CheckingAccount types are availiable to you beacuse you are {}".format(age))
                        accountSelect = 2
                    else:
                        # user will automatically be added to the customers list if they are not old enough to make an account
                        print(
                            "you are not old enough to open an account but you can join our customer list")
                        Customers[str(name)] = str(age)
                        accountSelect = 3

                    # casts input to float
                    type_of_acc = float(accountSelect)

                    # if user decides to make savings account
                    if (type_of_acc == 1):
                        print("selected SavingAccount")
                        #  assigns the Customer a random account number
                        AccountNum = str(random.randint(10000, 99999))

                        # assigns user random pin
                        UserPin = str(random.randint(1000, 9999))

                        # makes usre no duplicate accounts are given 
                        while 1:
                            if AccountNum in Accounts:
                                AccountNum = str(random.randint(10000, 99999))
                            else:
                                break



                        # assigns the cusomer a random iban composed of a random int number ans the fist letter of the users name
                        IBAN = "IEBOH" + \
                            str(random.randint(100000000, 999999999)) + \
                            str(name[0].capitalize())

                        # adds the user to the accounts and customers list
                        Accounts[str(AccountNum)] = SavingAccount(
                            name, age, AccountNum, IBAN, UserPin)
                        Customers[str(name)] = Customer(name, age)

                        # update the external files to include the new customers
                        UpdateAccounts()
                        UpdateCustomers()
                        UpdateAccountsTransaction

                        # prints the new users account details
                        print("here are your SavingAccount details\n")
                        print(Accounts[str(AccountNum)].myDetails())

                        break
                    # if user decides to make checking account
                    elif(type_of_acc == 2):
                        print("selected CheckingAccount")
                        #  assigns the Customer a random account number
                        AccountNum = str(random.randint(10000, 99999))
                        # assigns the cusomer a random iban composed of a random int number ans the fist letter of the users name
                        IBAN = "IEBOH" + \
                            str(random.randint(100000000, 999999999)) + \
                            str(name[0].capitalize())
                        
                        # assigns user random pin
                        UserPin = str(random.randint(1000, 9999))

                        # adds the user to the accounts and customers list
                        Accounts[str(AccountNum)] = CheckingAccount(
                            name, age, AccountNum, IBAN, UserPin)
                        Customers[str(name)] = Customer(name, age)

                        # update the external files to include the new customers
                        UpdateAccounts()
                        UpdateCustomers()

                        # prints the new users account details
                        print("here are your CheckingAccount details\n")
                        print(Accounts[str(AccountNum)].myDetails())

                        break
                    elif(type_of_acc == 3):
                        # update the external cusomters.txt to include the new customers
                        UpdateCustomers()

                        break
                    else:
                        # validation error message
                        print("not valid account type")

                except ValueError:
                    print("That's not a number!")

        # if user selctions option 2 from main menu
        elif option == 2:
            print('View Transactions \'Option 2\'\n')

            # identify the customer first
            # name = input("please enter your name: ")
            AccountNum_ = input("please enter your account number: ")
            AccountNum = int(AccountNum_)

            pinInput = input("enter your pin: ")



            # checks if the account number exits
            if (str(AccountNum) in Accounts) and (str(pinInput) == str(Accounts[str(AccountNum)].pin)) :
                print("we have that account number on file")
                print("Transactions on Account: {}".format(AccountNum))
                print(Accounts[str(AccountNum)].myTransactions())
            # if the account doesnt exit return appropriate error message
            else:
                print("that account number doesnt exist")

        # if user selctions option 3 from main menu
        elif option == 3:
            print('\nOperations Avalable to you \'Option 3\'')

            # prompt user to identify themself
            AccountNum_ = input("please enter your account number: ")
            AccountNum = int(AccountNum_)

            

            pinInput = input("enter your pin: ")




            if (str(AccountNum) in Accounts) and (str(pinInput) == (Accounts[str(AccountNum)].pin)):
                print("account  found")

                option_ = 0

                while(option_ != 6):


                    # displays the method operations menu
                    MethodMenu()
                    
                    # making sure everything is up to date
                    unpackFiles()

                    # asks the user to enter a menu option
                    option = input("enter method  menu option: ")
                    option_ = float(option)

                    if option_ == 1:
                        # output the users details
                        print(Accounts[str(AccountNum)].myDetails())
                    elif option_ == 2:
                        # propmt user to input deposit amount
                        inputNumber_ = input("enter your deposit amount: ")
                        inputNumber = float(inputNumber_)

                        # calls method to carryout deposit method
                        print(Accounts[str(AccountNum)].deposit(inputNumber))

                        # updates external files
                        UpdateAccounts()
                        UpdateAccountsTransaction()

                    elif option_ == 3:

                        # propmt user to input withdrawal amount
                        inputNumber_ = input("enter your withdrawal amount: ")
                        inputNumber = float(inputNumber_)

                        if Accounts[str(AccountNum)].AccountType == "SavingAccount":
                            # calls method to carryout withdrawal method
                            print(Accounts[str(AccountNum)
                                           ].withdraws(inputNumber))
                        else:
                            # calls method to carryout withdrawal method
                            print(Accounts[str(AccountNum)
                                           ].withdrawc(inputNumber))

                        # updates external files
                        UpdateAccounts()
                        UpdateAccountsTransaction()

                    elif option_ == 4:
                        # prints the users account balance
                        print(Accounts[str(AccountNum)].balance())

                    elif option_ == 5:
                        # prompt user to enter the desitnation Account number
                        destinationAccountNumber = input(
                            "please enter the desitnation Account Number: ")
                        print("\ntransfer ")
                        destinationIBAN = input("\nplease enter the desitnation Account IBAN: ")

                


                        # checks if account exists
                        if (str(destinationAccountNumber) in Accounts) and (str(destinationIBAN) == str(Accounts[str(destinationAccountNumber)].IBAN)) :
                            print("account  found")
                            # prompt user to enter transfer amount
                            amount = input(
                                "how much would you like to transfer: ")
                            amount = int(amount)

                            if Accounts[str(AccountNum)].AccountType == "SavingAccount":
                            # calls method to carryout transfers method
                                Accounts[str(AccountNum)].transfers(amount, str(destinationAccountNumber))
                            else:
                                # calls method to carryout transferc method
                                Accounts[str(AccountNum)].transfer(amount, str(destinationAccountNumber))

                            # updates external files
                            UpdateAccounts()
                            UpdateAccountsTransaction()
                        else:
                            # if account doesnt exist
                            print("Invalid destination details")
                    # returns user back to main menu
                    elif option_ == 6:

                        print("returning to main menu")
                    else:
                        print("not valid menu option")
            else:
                print("that account number doesnt exist")
        # if user selctions option 4 from main menu
        elif option == 4:
            print('Delete your account \'Option 4\'')
            AccountNum_ = input("please enter your account number: ")
            AccountNum = int(AccountNum_)

            pinInput = input("enter your pin: ")

            # checks if the account number exists or not

            if (str(AccountNum) in Accounts) and (str(pinInput) in str(Accounts[str(AccountNum)].pin)):
                print("account  found")

                # deletes the account the user enters
                del Accounts[str(AccountNum)]

                # updates the accounts and cusotmers file so changes persist
                UpdateAccounts()
                UpdateCustomers()
                UpdateAccountsTransaction()

                print("your account({}) has been succesfully deleted".format(
                    str(AccountNum)))

            else:
                print("that account number doesnt exist")
        # if user selctions option 5 from main menu
        elif option == 5:
            print("Thank you! exiting(5)")
            break
        # show user message if they enter a option outside the range of options
        else:
            print("Invalid option. Please enter a number between 1 and 5.")
    # if non numeric character in puted shows user appropriate message
    except ValueError:
        print("That's not a number!")
