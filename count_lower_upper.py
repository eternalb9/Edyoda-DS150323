#Program to count the upper and lower case of alphabets in a string.


def count_upper_lower(s):
    count_upper,count_lower=0,0
    for i in s: 
        if i.isupper():
            count_upper=count_upper+1
        elif i.islower():
            count_lower=count_lower+1    
    print("The number of Upper cases is ",count_upper)
    print("The number of Lower cases is ",count_lower)        
input_string=input("Enter the string : \n")
count_upper_lower(input_string)    