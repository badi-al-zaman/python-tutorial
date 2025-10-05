text = "Hello world!\n\t\b\sI am Mahmoud." # \n: new line, \t: tab, \b: backspace, \s: space

print(text[0:10]) # Slicing
text.lower()
text.upper()
text.title()
text.swapcase()

text.count(" ") # Return How Many spaces Is There In The Text
text.find("I") # Return The Index Of The First Match
text.replace("I", "i") # Replace All Matches
text.split(" ") # return words as a list

seperator = ";"
mylist = ["a", "b", "c"]
print(seperator.join(mylist))
print("{}".format(text))