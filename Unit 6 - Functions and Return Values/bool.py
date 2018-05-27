#Unit6 Program Assign
#Nazim HAMMICHE

#Compare function definition
def compare(a,b):
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0
#Greetings users and program introduction:
print("Welcome to UNIT 6 Programming Assignement. The purpose of this program is to allow you to compare two number A and B")
print("Before you can enter your own number let's text the program first!")

#Testting the all the fucntions possibilities
print (compare(5,2))
print (compare(2,5))
print (compare(3,3))

print("Everything is okay we can start !! ") #Confirm success to the user

#Promting the user:
a=input("Please enter your A number: ")
b=input("Please enter your B number: ")

#Display the result:
print("With : 1: A>B | -1:A<B | 0: A=B The result is: ") #Result explanation
print (compare(a,b))#Final result
print("THANK YOU ! ")
