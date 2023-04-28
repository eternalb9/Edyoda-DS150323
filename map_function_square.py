numbers=[int(x) for x in input("Enter the numbers separated by spacebar ").split()]
square_list=list(map(lambda x:x**2,numbers))
print("The Squares of the given numbers is",square_list)