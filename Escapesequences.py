#While printing Strings with single and double quotes in it causes SyntaxError
#because String already contains Single and Double Quotes and hence cannot be printed with the use of either of these
# Hence, to print such a String either Triple Quotes are used or Escape sequences are used to print such Strings
#Escape sequences start with a backslash and can be interpreted differently
#If single quotes are used to represent a string, then all the single quotes present in the string must be escaped and same is done for Double Quotes

#creating initial  String
String1=("I'm a Python developer\n")
print("The initial String is :-",String1)
#Escape sequences
String1=("I'm a Python \a developer\n")#ASCII Bell
print("The initial String is :-",String1)

String1=("I'm a \b Python developer\n")#ASCII Backspace
print("The initial String is :-",String1)

String1=("I'm a \r Python developer\n")#ASCII Carriage Return
print("The initial String is :-",String1)

String1=("I'm \\ Python developer\n")#Backslash
print("The initial String is :-",String1)

String1=("I'm a \'Python developer\'\n")#Single quote (')
print("The initial String is :-",String1)

String1=("I'm a \"Python developer\"")#Double quote(")
print("The initial String is :-",String1)

String1=("I'm a\''' Python developer\'''")#triple quote(''')
print("The initial String is :-",String1)

String1=("I'm a \fPython developer")#Formfeed
print("The initial String is :-",String1)

String1=("I'm a Python \tdeveloper")#ASCII Horizontal Tab
print("The initial String is :-",String1)

String1=("I'm a \v Python\v developer")#ASCII Vertical Tab
print("The initial String is :-",String1)

String1=("\100\101\103\104\105\106")#Character with octal value
print("The initial String is :-",String1)

String1=("\x45\x76\x100\x101\x102\x345") #Character with hex value
print("The initial String is :-",String1)

