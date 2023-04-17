#Program to to add the numbers in a list , numbers are taken from user and then stored inside a list.

def add(num_list):
    sum=0
    print("The Addition of the numbers present in above list is ")
    for i in num_list:
        sum=sum+i
    return print(sum)   


num_list=[]
num=int(input("How many numbers you want to get added\n"))
for i in range(1,num+1):
    c=int(input(f"Enter the {i} number  "))
    num_list.append(c)
print("Your required list is",num_list)
add(num_list)
