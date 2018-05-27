#Input: read the file
infile = open("unsorted_fruits.txt", "r")
fruit=infile.read()
fruit_list=fruit.split()

print("The full list")
print(fruit_list,"\n")


#Order the list:
fruit_list.sort()


#Input the alphabetcally ordered list the outputfile file
outfile=open("sorted_fruits.txt","w")
for word in fruit_list:
    outfile.write(word)
    outfile.write("\n")

print("Operation done. Please Open the file sorted_fruits.txt")

#Close the files
infile.close()
outfile.close()
