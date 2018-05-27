#Input: read the file
infile = open("unsorted_fruits.txt", "r")
fruit=infile.read()
fruit_list=fruit.split()

print("The full list")
print(fruit_list,"\n")


#Order the list:
fruit_list.sort()
print("Alphabetical order:")
print(fruit_list,"\n")


#print("List form:")
outfile=open("sorted_fruits.txt","w")
for word in fruit_list:
    print(word)
    outfile.write(word)
    outfile.write("\n")


#Close the files
infile.close()
outfile.close()
