import sys
import os
        
file_path=input("Enter the file_path:")
does_file_exist=os.path.exists(file_path)
print(does_file_exist)
if does_file_exist == False:
        print('Alert')
        sys.exit(0)