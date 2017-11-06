import os
path=input("Folder Name?")
files = os.listdir(path)
i = 1

for file in files:
    l=str(i)+"techstrav" + file[file.index('.'):]
    print(l)
    os.rename(os.path.join(path, file), os.path.join(path, l))
    i = i+1