print ("The program just started")

#Input and output files
f_in = open("/home/elemelons/unsorted_fruits.txt", "r")
f_out = open("/home/elemelons/sorted_fruits.txt", "w")

#Read the input file
fruits = f_in.readlines()

#Sort the list
fruits.sort()

#Write the sorted file
for fruit in fruits:
    if False == str.isspace(fruit):
        f_out.write(fruit)

#Close the input and output file
f_in.close()
f_out.close()
print ("The program ended")
