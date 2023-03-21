'''
-------------------------------------------------------------------------------
Name: Alexander Farouz
Assignment: PA 4
Due Date: 10/17/22
-------------------------------------------------------------------------------
Honor Code Statement: I received no assistance on this assignment that
violates the ethical guidelines set forth by professor and class syllabus.
-------------------------------------------------------------------------------
Comments and Assumptions: A note to the grader as to any problems or
uncompleted aspects of the assignment, as well as any assumptions about the #
meaning of the specification. You can write in N/A if you don’t have any
comments/assumptions.
-------------------------------------------------------------------------------
NOTE: width of source code should be <=80 characters to be readable on-screen.
12345678901234567890123456789012345678901234567890123456789012345678901234567890
10 20 30 40 50 60 70 80
-------------------------------------------------------------------------------
'''

'''
The following block of code goes through the indices of two lists, and stores
each index which has the same value in a new list then returns the list.

The outer for loop goes through the first list while the inner for loop
goes through the second list.

The if statement says if the index of the two lists is the same, and the
value assigned to those 2 indices is the same, then add the index number
to a new list. The break function resets outer for loop.
'''
def indices(some_list, another_list):
    new_list = []
    for i in range(len(some_list)):
        for j in range(len(another_list)):
            if some_list[i] == another_list[j] and i == j:
                new_list.append(i)
                break
    return new_list

'''
The following block of code is a function which contains three lists:
two of these lists contain integers, and the final list contains boolean
values.

The outer for loop goes through the first list while the inner for loop
goes through the second list. Meanwhile, there is a 3rd for loop inside
both of these which contains the boolean values.

Inside the boolean for loop, there is an if/elif statement which
determines whether to add the values assigned to the index of lists 1 and 2
togetherm or to subtract the values assigned to the index of lists 1 and 2.

If the value in the third list is TRUE, the code adds the two values
of the same indices and stores this value in a list. If the value in the
third list is FALSE, the code subtracts the two values of the same indices
and stores that value in a list. There are break statements under both the
if and elif statements to reset the outer for loop
'''
def compute(lst1, lst2, lst3):
    new_list = []
    for j in range(len(lst1)):
        for k in range(len(lst2)):
            for l in range(len(lst3)):
                if j == k and j == l and lst3[l] == True:
                    new_list.append(lst1[j] + lst2[k])
                    break
                elif j == k and j == l and lst3[l] == False:
                    new_list.append(lst1[j] - lst2[k])
                    break
            
    return new_list

'''
The following block of code is a function containg two lists and an integer
The point of the function is to determine the shorter list and replace
every nth index value with the corresponding index value from the longer
list. If the lists are equal in size, assume the first list is the smaller
list.

The if/else statement determines the smaller list which subsequently
determines which list needs to be modified. Inside each of these
statements, there is a for loop which goes through the length of each
list. Inside the for loops, there is an if/elif/else statement, which
determines the values which need to be returned in the resulting list.

The if statement determines whether the index value in the list which
needs modifying is the nth integer. If the index value is indeed the nth
integer, the value from the larger list is added to the resulting list.

The elif statement says if the integer value is 1, then print the larger
list.

The else statement says that if the index value of the smaller list is
not the nth integer, add the value of the smaller list to the resulting
list
'''
def replace_elems(lst1, lst2, n):
    new_list = []
    if len(lst1) > len(lst2):
        for j in range(len(lst2)):
            if ((j + 1) % n) == 0 and j != 0:
                new_list.append(lst1[j])
            elif n == 1:
                new_list.append(lst1[j])
            else:
                new_list.append(lst2[j])
    else:
        for j in range(len(lst1)):
            if ((j + 1) % n) == 0:
                new_list.append(lst2[j])
            elif n == 1:
                new_list.append(lst2[j])
            else:
                new_list.append(lst1[j])
    return new_list

'''
The following block of code is a function which has one list and
returns the number of coppies which that list contains

The is an outer foor loop which goes through the range of the length
of the list, and an inner for loop which goes through the range from
n to the length of the list.

Inside these for loops, there is an if statement which is true if
the values assigned to the indices are the same, but the indices
themselves are not the same. If it is true, the variable 'copy' is
incremented by 1 and the variable n is set to i + 1 to ensure that
the for loop does not go back over copies which it has already
accounted for.

The variable 'copy' is returned which has the number of copies which
were present in the list.
'''
def extra_copies(some_list):
    n = 0
    copy = 0
    for i in range(len(some_list)):    
        for j in range(n, len(some_list)):
            if i != j and some_list[i] == some_list[j]:
                copy += 1
                n = i + 1
                break
    return copy
