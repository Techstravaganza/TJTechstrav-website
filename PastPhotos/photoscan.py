import os, sys
year=input("Year?")
# Open a file
path = "images/Techstrav"+year
dirs = os.listdir( path )
put=open(year+"photolist.txt","w")

# This would print all the files and directories
put.truncate() #deletes all previous text in file
for file in dirs:
   put.write(file+"\n")
