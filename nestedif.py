age = 25
citizen = True

if age >=18:
    if citizen:
        print("you can vote")
    else:
        print("you must be a citizen to vote")
else:
    print("you are too yong to vote")            



age = 25
citizen = True

if age >=18 and citizen:
    if citizen:
        print("you can vote")
    
else:
    print("you are too yong to vote")      



#check even or odd number 
num = int(input("Enter a number:"))   

if num % 2==0:
    print(" even number")
else:
    print("odd number2")    

