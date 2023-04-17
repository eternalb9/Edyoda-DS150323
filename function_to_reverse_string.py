#Program to reverse a string using a user defined function.

string=input("Enter the string : \n")

def reverse(s1):
    s2=""
    for i in s1:
        s2= i+s2
    print("The reversed string is \n",s2)
reverse(string)    