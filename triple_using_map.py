numbers=[int(x) for x in input("Enter the numbers separated by spacebar ").split()]
triple_list=list(map(lambda x:x*3,numbers))
print("The Squares of the given numbers is",triple_list)