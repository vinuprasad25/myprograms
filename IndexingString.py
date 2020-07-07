                           #Indexing character in String

#In Python, individual characters of a String can be accessed by using the method of Indexing
#Indexing allows negative address references to access characters from the back of the String,
#-1 refers to the last character, -2 refers to the second last character
#While accessing an index out of the range will cause an IndexError
#Only Integers are allowed to be passed as an index, float or other types will cause a TypeError

#Create initial String
String1="Vinu Prasad"
print("The initial String:-",String1)

#Accessing first character in  string
print("the first character of string is:-",String1[0])

#Accessing middle  character in  string
print("the middle character of string is:-",String1[5])

#Accessing last character in String
print("the last character of string is:-",String1[10])

#Accessing first character in reverse
print("the first character of string in reverse:-",String1[-1])

#Accessing middle character  string in reverse
print("the middle character of string in reverse:-",String1[-5])

#Accessing reverse character in reverse
print("the last  character of string reverse:-",String1[-10])

#While accessing an index out of the range will cause an IndexError
#Accessing a character in  string
print("A character of string is:-",String1[11])

