import os, sys
# Open a file
path = "/images/Techstrav2015/"
dirs = os.listdir( path )
put=open("2015photolist.txt","w") 

# This would print all the files and directories
put.truncate() #deletes all previous text in file
for file in dirs:
   put.write(file)