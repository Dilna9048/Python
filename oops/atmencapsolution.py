# class ATM: 
#     def __init__(self, pin): 
#         self.__pin = pin 
 
#     def get_pin(self): 
#         return "PIN is protected. Cannot show." 
 
#     def change_pin(self, old_pin, new_pin): 
#         if old_pin == self.__pin: 
#             if len(str(new_pin)) == 4: 
#                 self.__pin = new_pin 
#                 print("PIN changed successfully") 
#             else: 
#                 print("PIN must be 4 digits") 
#         else: 
#             print("Wrong old PIN") 
 
# a = ATM(1234) 
# print(a.get_pin()) 
# a.change_pin(1234, 5678)


# bamnk  and atm pin
class BankAccount:
    def __init__(self, acc_holder,pin,balance=0):
        #private attributes 
        self.__acc_holder=acc_holder
        self.__pin =str(pin)
        self.__balance=float(balance)
        self.__pin_attempts=0
        self.__max_attempts=3
        self.__locked=False
        
    def __verify_pin(self, pin_input):
        if self.__locked:
            print("account is locked ")
            retun
        if str(pin_input) == self.__pin:
            self.__pin_attempts=0
            return True
        else:
            self.__pin_attempts+=1
            attempts_left=self.__max_attempts-self.__pin_attempts
            if attempts_left<=0:
                self.__locked=True
                print("Incorrect PIN, account Locked..! ")
            else:
                print(f"incorrect PIN attempts left : {attempts_left}")
            return False
            
    def  check_balance(self,pin_input):
        if self.__verify_pin(pin_input):
            print(f"Available Balance : rs.{self.__balance:.2f}")
            return self.__balance
        return None

    def change_pin(self,current_pin, new_pin):
        if not (str(new_pin).isdigit() and len(str(new_pin))==4):
            print("pin must be exactly 4 digits.")
            return False
        if self.__verify_pin(current_pin):
            self.__pin=str(new_pin)
            print("pin changed successfully")
            return 
        return False

acc=BankAccount("Anu",pin=1234,balance=50000)
while True:                   
    print("\n==== ATM MENU ====")
    print("1. Check Balance")
    print("2. Change PIN")
    print("3. Exit")
    choice = input("choose (1-3): ").strip()

    if choice == '1':
        pin=input("Enter a pin : ")
        acc.check_balance(pin)
    elif choice == '2':
        c_pin=input("Enter current  pin : ")
        n_pin=input("Enter new  pin : ")
        acc.change_pin(c_pin,n_pin)
    elif choice=='3':
        print("exit....")
        break
    else:
        print("invalid choice..")