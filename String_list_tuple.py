"""
program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')

"""

values=input("Enter some comma-separated values :")

#using split function of list ,split the string "values" and store in variable list

list=values.split(",")


#converting list into tuple

Tuple=tuple(list)




#Print list

print("List :",list)


#Print Tuple

print("Tuple :",Tuple)
