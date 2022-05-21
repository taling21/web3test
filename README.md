In my code , the first class is the 'bank' - and it has 'lender' as its child. The various lenders are the objects of this 'lender' class. The borrower will be an object of the 'borrower' class. The 'bank' class is an abstract one,so it can't be instantiated  directly. The program takes the name of the borrower and money requirement as input, and returns the "most suitable lender". The most suitable lender is the one with sufficient money to lend, at the lowest rate of interest. 
The algorithm to decide the suitable lender is : out of the List of lenders, put those in a dictionary which are eligible, then find the minimum value in the dictionary. The dictionary here, is an object of my_dictionary class.

To run the code, compile and execute the code on a suitable platform , and input the name and money required. The details of the most suitable lender will be displayed.To run in the CMD, type 'python file_name.py'


The Loaning system implemented is centralized, as the 'bank' acts as the exchange. The bank has the data of all lenders, and it is the bank which has decided the algorithm for loaning system. All transactions are intermediated by the bank, hence it is a centralized system. All the finance activities(here,lending) goes through the central agency - the 'bank'.


Demerits of a centralized system :
 You don’t own a private key that gives you access to your wallet. 
 
 Furthermore, the exchange determines which coins they list for trading or how much fees you have to pay to trade using their exchange.

 You don’t truly own your cryptocurrencies when trading via a centralized exchange.
 
 Moreover, you are subject to the rules a centralized exchange imposes on you.

