readme = open("README.md", "r") # Open the file in read mode. modes are "r", "w", "a", "r+", "w+", "a+"
content = readme.read()
print(content)
readme.close()

with open("README.md", "r") as readme: # Open the file in read mode
    content2 = readme.read()
print(content2)

# It's a good practice to use 'with' statement when dealing with file operations
with open("example.txt", "w") as example_file: # Open the file in write mode
    example_file.write("This is an example file.\n")
    example_file.write("It contains multiple lines of text.\n")
    # example_file.write("Hello!")
    # example_file.flush() # Execute All Previous Operations On The Local File because It's still in the buffer memory
    # note if the file not exist, and you used writing or Appending mode it will create the file

from os import *
# mkdir("Test Folder") # Create A Directory On The Script Path
# chdir("Test Folder") # Change The Working Directory
# rename("file_name", "new_file_name") # Rename A File Or Directory
# remove("Test Folder")