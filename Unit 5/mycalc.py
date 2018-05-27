#Greeting the Users ! 
print("Welcome to UoP Calculator! We will help you make easy calculation easier to do!")
print("-------------------------------------------------------------------------------")
print("To start Select your first Number!")

#Part 1 : Input Data from user.

#Promting the first number and controle user input
numberA=input("1st Number: Enter a number different from 0: ")


while numberA == '0':
    print("Please enter a number that is different from 0!")
    numberA=input("Try Again! You Can Do it ;)")
    int(numberA)
    
numberA=int(numberA)
print("You entered",numberA,"Good Job!")

#Promting the operation and control user input
print("Now,please select your operation by entering it's corresponding number: ")
operation=input("1-add, 2-subtract, 3-multiply, 4-divide: ")

while operation !='1' and  operation !='2' and  operation !='3' and operation !='4':
    print("Please select the right operation number from 1 to 4. We believe in you ;)")
    operation=input("Reminder ! 1-add, 2-subtract, 3-multiply, 4-divide: ")
    int(operation)

print("Thank You!")

#Promting the second number and control user input
numberB=input("2nd Number: Enter a number different from 0: ")


while numberA == '0':
    print("Please enter a number that is different from 0!")
    numberB=input("Try Again! You Can Do it ;)")
    
numberB=int(numberB)       
print("You entered",numberB,"Good Job!")

#Part2: Process user datas

if operation == '1': #Add
    Result=numberA+numberB
    print("Your operation is the following addition: ",numberA,"+",numberB)
elif operation == '2':#subtract
    Result=numberA-numberB
    print("Your operation is the following substraction: ",numberA,"-",numberB)
elif operation == '3':#multiply
    Result=numberA*numberB
    print("Your operation is the following mutiplication: ",numberA,"*",numberB)
else: #divide
    Result=numberA/numberB
    print("Your operation is the following mutiplication: ",numberA,"/",numberB)

#Part 3 : Display Final result:

print("The result is : ",Result)
