#Parent class. Bank registration demo, asking for user info and deposit.
class Bank():
    all = {}
    def __init__(self):
        quiet = []
        while len(quiet ) < 3:
            self.name = input("Welcome to EnvBa! \nWhats is your full name:").title()
            quiet.append(self.name)
            self.age = int(input("Welcome " + self.name +"! What is your age?"))
            assert self.age >0, "Only positive numbers are allowed"
            quiet.append(self.age)
            self.gender = input("Perfect. What is your gender?").title()
            quiet.append(self.gender)

        self.balance = 0

    def show_details(self):
        print("Personal Details")
        print("")
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Gender: ", self.gender)


    def deposit(self):

        self.amount = float(input("Ok " + self.name + ", How much money do you want to deposit:"))
        self.amount = float(self.amount)
        assert self.amount > 0, "Only positive numbers are allowed"
        self.balance = self.balance + self.amount
        print("Account balance has been  updated : $", self.balance)

#Not using it in this example. It allowing the user to withdraw money from his account.
    def withdraw(self, amount):

        self.amount = amount
        if self.amount > self.balance:

            print("Insufficient funds | Balance Avilable : $", self.balance)
        else:

            self.balance = self.balance - self.amount
            print("Account balance has been updated : $", self.balance)

    def view_balance(self):
        self.show_details()
        print("Account balance : $", self.balance)

#Child class. Letting the user the option to put a certain amount in an digital envelope. 
#The money will be used only according to envelope catagory.
#As of now, I made only 4 catgories, that you can see in the end of the code when calling the functions line 185 and on.
class Envelope(Bank):
  def __init__(self):
    super().__init__()

    self.env_balance = 0

  def envelope_deposit(self, envelope, env_deposit):
    self.envelope = envelope
    self.env_deposit = env_deposit

#Adding to dictionry "all"
    Bank.all[envelope] = env_deposit

#Envelope creation setup. Checking that the envelopes deposit are not bigger than avaliable balance.
    if self.env_deposit > self.balance:
      print("Envelope couldn't recive the fund. Insufficient funds | Balance Avilable : $", self.balance)

    else:
      self.env_balance = self.env_deposit
      print("You created an envelope name: " +  self.envelope, ".", "Your envelope contain: $" + str(self.env_balance))
      self.balance = self.balance - self.env_deposit
    print("Your account balnace is now: $" + str(self.balance), "And $" + str(self.env_balance), " In the " + self.envelope, " envelope")

  def __repr__(self):
      return f"Envelope: {self.envelope}, {self.env_deposit}"


# Function to transfer money from one envelope to the other. Not using it in this examaple for now.

  def env_transfer (self, from_env, amount, to_env):

     if from_env in Bank.all and to_env in Bank.all:
        if Bank.all[from_env] < amount:
            print("Insufficient funds | Balance Avilable : $" + str(Bank.all[from_env]))


        else:
            Bank.all[from_env] = Bank.all[from_env] - amount
            Bank.all[to_env] = Bank.all[to_env] + amount
            print(from_env + " New amount: " + str(Bank.all[from_env]) + " " + to_env + " New amount: " + str(Bank.all[to_env]))

     elif from_env == "Main Balance":
         if self.balance < amount:
             print("Insufficient funds | Balance Avilable : $" + str(self.balance))
         else:
             self.balance = self.balance - amount
             Bank.all[to_env] = Bank.all[to_env] + amount
             print(from_env + " New amount: " + str(self.balance) + " " + to_env + " New amount: " + str(Bank.all[to_env]))

     elif from_env not in Bank.all and to_env in Bank.all:
        print("The envelope: " + from_env + " is not created.")
     elif from_env in Bank.all and to_env not in Bank.all:
        print("The envelope: " + to_env + " is not created.")
     else:
         print("Envelopes " + from_env + " and " + to_env + " are not created")

#Grandchild class. Buying system. It's get the user input regarding the store that he bought and the amount spend.
#If it's recognize the store, it's taking the money out from the correct envelope.
#If it doesn't recognize, it's taking money from the main balance.
#As of now, there's a very limit amount of recognized stores. You can see them in the buying_code dictionary.
class Buy(Envelope):
    #Every catagory of store have is on buying code, that the program can identify.
    #First one is for "groceries". Second for "bills". third for "Shopping". fourth for "Travel".
    buying_code = {
    "Qwg24" : ["Trader Joe's","Shop Rite", "Walmart", "Stop & Shop"],
    "Qwb45" : ["Seg", "Ui", "Con Edison", "Ultra Mobile", "Visible Mobile"],
    "Qws88" : ["Amazon", "Nike", "Ralph Luren", "Macy's", "Apple"],
    "Qwt95" : ["Uber", "Lyft", "Southwest", "American Airlines", "Air France"]
    }
    def __init__(self):
      super().__init__()

    def buying_system(self, store, price):
        check_list = []

        self.store = store
        self.price = price

     #Checking if the store input is in the dictionary. If yes it's append the buying code to a list.
     #Then have if statments to check what is the code in the list.
     #And according to the code, recognize what envelope it's belongs to.
     #Then checking if the paid amount is available in the envelope. 
     # If yes, the buying worked. If not the user will get a message that it doesn't worked and how much money is available.
        for key, value in Buy.buying_code.items():
            if self.store in value:
                check_list.append(key)

                if "Qwg24" in check_list:
                    print("You're buying groceries")
                    if Bank.all["Groceries"] < self.price:
                        print("Insufficient funds | Avilable Balance: $" + str(Bank.all["Groceries"]))
                    else:
                        Bank.all["Groceries"] = int(Bank.all["Groceries"] - self.price)
                        print("You're reminded balnace in Groceries is :$" + str(Bank.all["Groceries"]))
                    #Bank.all["Groceries"] = int(Bank.all["Groceries"]) - self.price
                    #print(Bank.all["Groceries"])

                elif "Qwb45" in check_list:
                    print("You're paying bills")
                    if Bank.all["Bills"] < self.price:
                        print("Insufficient funds | Avilable Balance: $" + str(Bank.all["Bills"]))
                    else:
                        Bank.all["Bills"] = int(Bank.all["Bills"] - self.price)
                        print("You're reminded balnace in Bills is :$" + str(Bank.all["Bills"]))
                    #Bank.all["Bills"] = int(Bank.all["Bills"]) - self.price
                    #print(Bank.all["Bills"])

                elif "Qws88" in check_list:
                    print("You're doing shopping!")
                    if Bank.all["Shopping"] < self.price:
                        print("Insufficient funds | Avilable Balance: $" + str(Bank.all["Shopping"]))
                    else:
                        Bank.all["Shopping"] = int(Bank.all["Shopping"] - self.price)
                        print("You're reminded balnace in Shopping is :$" + str(Bank.all["Shopping"]))

                elif "Qwt95" in check_list:
                    print("You're going to travel!")
                    if Bank.all["Travel"] < self.price:
                        print("Insufficient funds | Avilable Balance: $" + str(Bank.all["Travel"]))
                    else:
                        Bank.all["Travel"] = int(Bank.all["Travel"] - self.price)
                        print("You're reminded balnace in Travel is :$" + str(Bank.all["Travel"]))

     #If the store is not in the dicionary, so no code appended to the list.
     #Then the money will go out from the genaral balance, if he have available founds.
        if not check_list:
            print("Unrecognized catagory. withdrawing from main balance")
            if self.balance < self.price:
                print("Insufficient funds | Avilable Balance: $" + str(self.balance))
            else:
                self.balance = int(self.balance) - self.price
                print("You're reminded balnace in your main balance is :" + str(self.balance))



#Calling the first function, to get user info and deposits
b = Buy()
b.deposit()
b.show_details()

#Getting user input for using the digital envelopes
env1 = float(input("How much money do you want to deposit to the groceries envelope? "))
assert env1 >0, "Only positive numbers are allowed"
env2 = float(input("How much money do you want to deposit to the bills envelope? "))
assert env2 >0, "Only positive numbers are allowed"
env3 = float(input("How much money do you want to deposit to the shopping envelope? "))
assert env3 >0, "Only positive numbers are allowed"
env4 = float(input("How much money do you want to deposit to the travel envelope? "))
assert env4 >0, "Only positive numbers are allowed"
b.envelope_deposit("Groceries", env1)
b.envelope_deposit("Bills", env2)
b.envelope_deposit("Shopping", env3)
b.envelope_deposit("Travel", env4)

#Asking about what store he bought and amount
store = input("What store are you buying from : ").title()
price = float(input("How much did you paid : "))
assert price >0, "Only positive numbers are allowed"
b.buying_system(store, price)

#While loop, to continue the program until he decied to quit.
active = True
while active == True:
  finish = input("Anything else that you want to buy? (y/n) ").lower()
  if finish == "y":
    store = input("What store are you buying from : ").title()
    price = float(input("How much did you paid : "))
    b.buying_system(store, price)

  else:
    print("Ok, see you next time!")
    active = False


  
