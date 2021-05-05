import os
path=input("Enter the path:")
filename=input("Enter Filename:")
full_path=[]
for r,d,f in os.walk(path):
    if filename in f:
        full_path.append(os.path.join(r,filename))
        if full_path==[]:
            print("File Not Found")
        else:
            print("Fullpath of File is "+str(full_path[0]))