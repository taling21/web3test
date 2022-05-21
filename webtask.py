from abc import ABC, abstractmethod




class bank(ABC):                    # class bank has child - lender

    def __init__(self):          #this method is in parent class as well as child class - Polymorphism 
        print("hello")
        self._locker = 2              #protected member
    def naming(self,ids,name):    
          self.Name = name
          self.empid = ids
    @abstractmethod                #abstracttion
    def fn(self):
          pass

class lender(bank):
           def __init__(self,amount,empint,his_id,lname) :        #__init__ function is executed whenever an object is created 
             self.canlend = amount
             self.interest = empint
             bank.naming(self,his_id,lname)
           def __del__(self):                                                     #in python, objects are automatically destroyed when not enough instances
                print( lname,"is being automatically destroyed. Goodbye!")
           def fn(self):
               print("The abstract method")
                                                     # instance variables belong to objects, not to class. So for lender1,lender2,... canlend and other variables have different values
class borrower:
    def __init__(self):
        pass
    def data():
        needs = breq   
        borname = bname

        
class my_dictionary(dict):
  
    # __init__ function
    def __init__(self):
        self = dict()                         #creating a class to help in adding new elements in dictionary
          
    # Function to add key:value
    def add(self, key, value):
        self[key] = value
  



lender1 = lender(50000,10,73,'Sheldon')
lender1.fn()   #showing the abstract function 
lender2 = lender(100000,12,37,'Leonard')
lender3 = lender(25000,3,21,'Raj')
lender4 = lender(130000,20,12,'Howard')
lender5 = lender(200000,25,59,'Penny')

list = [lender1,lender2,lender3,lender4,lender5]

dict_obj = my_dictionary()                          #creating a dictionary to store eligible lenderers
borr = borrower()
borr.name = eval(input("Enter your name:"))
borr.needs = eval(input("Enter the amount needed:"))
for i in range(5):
    if list[i].canlend >= borr.needs:
        dict_obj.add(list[i].Name,list[i].interest)
if (len(dict_obj) == 0):
    print("Sorry, none can fulfill your demand")
else:
        mini = min(dict_obj.values())
        minkey = min(dict_obj, key=dict_obj.get)
        print("The best suited lender for you is ",minkey)
        print("And the interest to pay is ",mini,"%")
  
