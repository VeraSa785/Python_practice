# function which generates a sequence of odd numbers ranging
# from a to b (a and b inclusive)

# without list comprehensions
def list_odd_numbers (a = 0 , b = 0):
    number_list = []
    for number in range(a,b+1):
        if number % 2 != 0:
            number_list.append(number)
    print(number_list)
list_odd_numbers(3,17)

# with list comprehensions
def list_odd_numbers (a = 0 , b = 0):
    number_list = [ number for number in range(a,b+1) if number % 2 != 0 ]
    print (number_list)
list_odd_numbers(3,17)
