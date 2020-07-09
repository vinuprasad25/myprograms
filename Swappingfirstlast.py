#Swapping First and Last character in String
def swap_string(str):
    if len(str) <= 1:
        return str

    mid = str[1:len(str) - 1]
    return str[len(str) - 1] + mid + str[0]


print (swap_string('Vinu Prasad'))
print (swap_string('vignesh prasad'))
print (swap_string('python'))
print (swap_string('developer'))

#Second Approach
string1 = input("Enter a string : ")
new_str = string1[-1:] + string1[1:-1] + string1[:1]
print(new_str)