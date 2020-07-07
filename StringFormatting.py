#Formatting String
#Strings in Python can be formatted with the use of format() method which is very versatile and powerful tool for formatting of Strings
#Format method in String contains curly braces {} as placeholders which can hold arguments according to position or keyword to specify the order
#default  String

#Syntax : {0} {1}.format(positional_argument, keyword_argument)

String1 = "Vinu Prasad is a python developer"
print("The default String is:-",String1)
#default order
String1="{} {} {} {} {} {}".format('Vinu', 'Prasad', 'is', 'a', 'python', 'developer')
print("the default order of the string is ",String1)

#positional Formatting
String1="{1} {2} {3} {4} {5} {0}".format('Vinu', 'Prasad', 'is', 'a', 'python', 'developer')
print(" ",String1)

#keyword Formatting
String1="{p} {i} {a} {y} {d} {v}".format(v='Vinu', p='Prasad', i='is', a= 'a',  y='python', d='developer')
print(String1)

#Binary Formatting
String1 = "{0:b}".format(25)
print("the binary formatting of 25",String1)

#decimal Formatting
String1 = "{0:d}".format(25)
print("the decimal formatting of 25",String1)

#octal formatting
String1 = "{0:o}".format(25)
print("the octal formatting of 25",String1)

#hex decimal formatting
String1 = "{0:x}".format(25)
print("the hex decimal formatting of 25",String1)

#Float formatting
String1="{0:e}".format(1652.32658)
print("The Exponent form",String1)

#Intgers Round-off
String1 = "{0:.3f}".format(1/7)
print("round of 1/7:-",String1)

#String Alignment
String1 = "|{:<10}|{:^10}|{:>10}|".format('Prasad', 'python', 'developer')
print("left center right alignment with formatting:-",String1)

#aligning of spaces
String1 = "\n{0:^20} was founded in {1:<4}!".format("Python Programming", 1991)
print(String1)


#formatting was done without the use of format method by using % operator
Integer = 12.3455657
print("formatting in 3.3f format:=")
print('the value of integer is:-%3.2f' %Integer)
print('the value of integer is:-%3.4f' %Integer)
