#Find The Longest String in Given List.
StringList = ['Vinu','is','a','python','developer']
print("The initialized string in given string is:-",StringList)
result = max(StringList, key =len)#using max function
print("the longest String in given list is:-",result)

#2ND Approach
# Find the shortest string in given List
StringList = ['Vinu','is','a','python','developer']
print("The initialized string in given string is:-",StringList)
result = min(len(ele) for ele in StringList) #using min function
print("the Shortest  String in given list is:-",result)