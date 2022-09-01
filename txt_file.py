# a function to read the .txt file line by line
# names_file = open("names.txt", "r")
# def file():
#     print(names_file.readline())
# file()
# file()


    



# How to read, write  a .txt file in python
# create the .txt file in the same folder where the .py file is located
# create a variable for the .txt file and use the open function. the r stands for read
# "w " stands for write, 'r+' stands for read and write, "a" stands for append
#names_file = open("names.txt", "r")
# to check if the .txt file is readable 
#print(names_file.readable())
# to read the file 
#print(names_file.read())
# to print the .txt file line by line. i created a function above for the readline statment
#print(names_file.readline())
# to close the .txt file
#names_file.close()


# Writing and appending to a .txt file
names_file = open("names.txt", "a")
# when you use w it clears all the data in thre existing file
# to add a new txt to the file
names_file.write("\ngod is faithful")
#to create a new file with w
names_file= open("")
names_file.close()





