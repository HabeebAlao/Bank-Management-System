# Bank-Management-System

**Description of** **the project classes and its methods** 

 

This bank management system, This project consists of 6 classes which are named Bank, BankBranch, Customer, Account , SavingAccount and checkingAccount. 

The Bank class simply holds some information about the bank headquarter including the banks name and the headquarter address. 

The BankBranch class holds information about the bank’s branch like the bank name which is inherited form the bank class, the bank address email and contact number. these are all private attributes.

next I have a customer class which inherits all the information from the bank branch class.

it stores information such as the name the age the email and the address of the customer

The initialization of these attributes is done in the __init__ function the other remaining final method is the __str__ method which returns the customer's name and age.

the next class we have is the account's class this inherits all the customer's information and attributes using the Super function in the __init__ method It also stores the users IBAN account number on funds. There is a total of eight methods in the account class they consist of myDetails method, myTransactions, balance, deposits, withdraw, transfer method and the __str__ method.

**User manual**

upon first run of the program you will be shown a main menu from which are 5 options. You must enter a corresponding number to the menu and press enter.

You may be prompted to enter an account number you simply enter the account number and press enter. Likewise if you are prompted to enter a cash amount enter the numeric value and press enter.

The accounts.txt file holds the users info you can find the user pin in here, the accountstransactions.txt hold the users transactions and the customers file hold all customers even if they are not able to make an account.

**Difficulties and more challenging parts**

the most challenging aspects of the project I found difficulties with would be unpacking and updating external files in a way that would be modular and would abide by good coding conventions, also learning to use the tabulate module to display the transactions in the way I wanted.one of the more difficult challenges was figuring out how to make only one out transaction per month as I had to learn how date objects worked and how to manipulate them in a way that worked for the program
