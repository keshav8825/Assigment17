''' Write a python program to add items from another set to the current set. thisset =
{"Java", "Python", "SQL"}
secondset= {"C", "Cpp", "NoSQL"} '''
thisset ={"java","python","SQL"}
secondset= {"c","Cpp","NoSQL"}
print(thisset)
thisset.pop()
print(thisset)
thisset.update(secondset)
print(thisset)