               #UPDATING STRING
#In Python, Updation or deletion of characters from a String is not allowed
#This will cause an error because item assignment or item deletion from a String is not supported
#Although deletion of entire String is possible with the use of a built-in del keyword
#This is because Strings are immutable, hence elements of a String cannot be changed once it has been assigned
#Only new strings can be reassigned to the same name
#initial string
String1=("Hello vinu prasad!!!")
print("the initial string:-",String1)


#updating entire string
String1=("vignesh prasad")
print("the updated string is:-",String1)

#we can re-assign string
String1=("Hello vinu prasad!!!")
print("The re-assigned string is:-",String1[:5]+ 'vignesh')

#updating character in string
String1[7]='K'