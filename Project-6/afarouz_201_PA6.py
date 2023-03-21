'''
-------------------------------------------------------------------------------
Name: Alexander Farouz
Assignment: PA 6
Due Date: 11/9/22
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
The parameters for the following function consists of 1 positional paramater
'elems' which is a list, and 2 keyword paramters: 'rt_shift' and 'filler'.

The positional argument elems is returned, while rt_shift and filler modify
elems. The default value for rt_shift if not given in the calling of the
function is 1, meaning one value at the end of the list is removed and the
value assigned to filler is added to the front of the list.

The default value for filler if not given in the calling of the function is
"X", which replaces the values which are displaced

The last elif and else statements decide if rt_shift is less than or equal
to the length of the list elems. If it is less, a for loop for the range of
the rt_shift is executed, and each time the last element in the list is
deleted and the value assigned to filler is inserted into the beginning of
the list.

If the rt_shift value is greater than the length of the list, the list is
replaced with the filler values.
'''
def shift_elems(elems, rt_shift = 1, filler = 'X'):
    if len(elems) == 0:
        return elems
    elif rt_shift == 1:
        del elems[-1]
        elems.insert(0, filler)
        return elems
    elif rt_shift <= len(elems):
        for i in range(0, rt_shift):
            del elems[-1]
            elems.insert(0, filler)
        return elems
    else:
        for i in range(len(elems)):
            del elems[0]
            elems.append(filler)
        return elems

'''
The following definition finds the mode in a given list.

2 empty lists are declared, count_list and copy_list. The first for loop
creates a copy of list1, which is used later. The second for loop goes through
all the values in the given list and sees how many times that value is
repeated. If it is repeated, the count goes up by 1 for each duplicate. After
going through the whole list. The value being evaluated is replaced with an
underscore, and the count is added to count_list and the for loop continues

The next for loop goes through count list and sees if there are are any
values in it which are not 0. If there  are, the boolean 'zero_bool' is made
True and the loop breaks

The next for loop finds the maximum value in the count list. finally, the
last for loop goes through the count list and contains an if/elif statement.
If the current iteration of count list is equal to the maximum count and max
count is not 0, the corresponding value in copy list is added to list2, the
return list. The elif says if zero_bool is false, return the original list.
'''
def find_mode(list1):
    count_list = []
    copy_list = []
    for i in range(len(list1)):
        copy_list.append(list1[i])
    for i in range(len(list1)):
        count = 0
        for j in range(len(list1)):
            if list1[i] == list1[j] and i != j:
                count += 1
        list1[i] = '_'
        count_list.append(count)    
    
    
    zero_bool = False
    for i in range(len(count_list)):
        if count_list[i] != 0:
            zero_bool = True
            break
    
    list2 = []
    max_count = 0    
    for i in range(len(count_list)):
        if count_list[i] > max_count:
            max_count = count_list[i]
    
    for i in range(len(count_list)):
        if max_count == count_list[i] and max_count != 0:
            list2.append(copy_list[i])
        elif zero_bool == False:
            list2.append(copy_list[i])
    
    return list2

'''
The following definition finds the median of a given list.

The while loop checks if the length of the list is greater than 2. If it is,
the first and last elements of the list are deleted. This continues until the
list is either a length of 2 or 1.

The if/elif statement checks if the length of the list is 1 or 2. If its 1,
the value in the list is returned. If it is 2, the middle point between the
two values is found and returned
'''         
def find_median(list1):
    while len(list1) > 2:
        del list1[-1]
        del list1[0]
    if len(list1) == 2:
        return (list1[0] + list1[1]) / 2
    elif len(list1) == 1:
        return list1[0]
    
'''
The following block of code finds the mean, median, and mode of a given list.

The first for loop creates two copies of the given list so they can be used
when the definitions are called in the dictionary.

The following for loop goes through the list and finds adds all the values in
the given list and stores the value in numer

Finally, there is an if/else statement. If the given list is empty, then the
mean is returned as None. Otherwise, the mean is equal to the sum of the
values in the list divided by the length of the list rounded to 2 decimal
places.

A dictionary with keys 'mean', 'median' and 'mode' is returned with the
corresponding values assigned to each key.
'''
def averages(list1):
    mode_list = []
    median_list = []
    for i in range(len(list1)):
        mode_list.append(list1[i])
        median_list.append(list1[i])
    numer = 0
    for i in range(len(list1)):
        numer += list1[i]
    if len(list1) == 0:
        avg = None
    else:   
        avg = round(numer/len(list1), 2)
    
    
    new_dict = {'mode': find_mode(mode_list),
                'median': find_median(median_list),
                'mean': avg}
    
    return new_dict

'''
The following definition is a helper function for the add_chars definition.

If the length of some_str is greater than or equal to the length of some_list,
this function is initiated.

The first if statement checks if the length of the list is less than the
length of the string. If it is, the string is shortened so that it does not
exceed the length of the list. Now the length of the string is equal to that
of the list

After this initial if statement, there is an if/elif/else statement. The if
and elif statements are base cases, which return the list if it is empty, or
if the string is empty.

The else statememt contains another if/elif/else statement. The if statement
checks if the list has been modified yet. If it has not, then the first
character in the string is added as the second element in the list. The elif
statement checks if the length of the string is equal to 1. If it is, then
the last character of the string is added to the list. Finally, the else
statement determines how much of the string is left and depending on the
length of the string, it is added to its designated spot in the list.

Afterwards, the element which was just added in the string is removed from
the string, and the function is executed until the string is empty, then
returns the list.
'''
def add_chars_helper(some_list, some_str):
    if len(some_list) < len(some_str):
        some_str = some_str[0:len(some_list)]
    if some_list == []:
        return some_list
    elif some_str == '':
        return some_list
    else:
        if len(some_str) == len(some_list):
            some_list.insert(1, some_str[0:1])
        elif len(some_str) == 1:
            some_list.append(some_str[0:1])
        else:
            some_list.insert(-len(some_str)+1, some_str[0:1])
        some_str = some_str[1::]
        return add_chars_helper(some_list, some_str)
    
'''
The following function is for when the length of the string is less than the
length of the list. The first two if statements are base cases.

The following if/elif/else statement determines what to do with the input
values. The else statement is for if the length of the string is greater than
or equal to the length of the list. It initiates the add_chars_helper
function The elif statement says if the length of the list is greater than
the length of the string, add the string 'Commence' to the end of some_str,
then call the function again.

Finally the if statement has another if/else conditional under it.

The if statement returns some_list if the original input for some_str no
longer exists. The else statement finds the difference between the length
of the list and the original string, then uses this value to insert the
first character of the string into the appropriate position. Afterwards,
the character which was inserted is then deleted, and the function calls
itself.
'''
def add_chars(some_list, some_str):
    if some_list == []:
        return some_list
    if some_str == '':
        return some_list
    
    if 'Commence' in some_str:
        if some_str == 'Commence':
            return some_list
        else:
            divider = len(some_list) - (len(some_str)-8)
            some_list.insert(divider-1, some_str[0:1])
            some_str = some_str[1:]
            return add_chars(some_list, some_str)
    elif len(some_list) > len(some_str):
        some_str += 'Commence'
        return add_chars(some_list, some_str)
    
    else:
        return add_chars_helper(some_list, some_str)


