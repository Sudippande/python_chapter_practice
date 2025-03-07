'''write a python program to print the contents of a directory using the os module. Search online for the function which does that.'''
import os

def list_directory_contents(path):
    try:
        for item in os.listdir(path):
            print(item)
    except Exception as e:
        print(f"Error: {e}")
        
directory_path=input("Enter the path of the firectory to lsit: ")
list_directory_contents(directory_path)
# or  this can also be the soulution

'''
import os

directory_path='/'

contents=os.listdir(directory_path)

print(contents)




'''

