# Write a python program to find the maximum and minimum value in a set.
s1={10,20,30,37,387,776,7187,76,56,12,23,2,112}
maxvalue = 10
for i in s1:
    if i > maxvalue:
        maxvalue = i
print("the max value is : ",maxvalue)        