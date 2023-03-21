'''
-------------------------------------------------------------------------------
Name: Alexander Farouz
Assignment: PA 7
Due Date: 11/23/22
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
The try/except ensures that a feesible file is used. If the file is not found
then the function will return 'File Not Found.

The first three lines under the try statement open the file and iterates
through each line of the file. The first line under the for loop splits each
individual line into a list.

The if statement checks if that specific line's name is the same as the input
name. If it is, the precinct is stored in prec and then the loop is broken
and the name with the corresponding precinct is returned
'''
def voterPrecinct(voterFile, voterName):
    try:
        file = open(voterFile, 'r')
        file = file.readlines()
        for i in range(len(file)):
            new_line = file[i].split(',')
            if new_line[0].lower() == voterName.lower():
                prec = new_line[3]
                prec = prec.strip('\n')
                break
        return 'Name: '+new_line[0]+' '+'Precinct: '+prec
    
    except FileNotFoundError:
        return 'File Not Found'

'''
The try/except ensures that a feesible file is used. If the file is not found
then the function will return 'File Not Found.

The initial for loop and the two lines above iterare through each line in the
spreadsheet. The nested for loops go through each character in the name of
the line and removes the characters which are in the initially defined list
'remove'.

The second set of nested for loops capitalizes each element in new line in
order for it to match the proper output.

The final if statement returns the precinct, the polling place, the address,
and the city.
'''
def findPrecinctInfo(precFile, precName):
    remove = ["#", "!", "$", "%", "&", "*", "^"]
    try:
        file = open(precFile, 'r')
        file = file.readlines()
        for i in range(len(file)):
            new_line = file[i].split(',')
            for j in range(len(new_line)):
                for k in range(len(remove)):
                    if remove[k] in new_line[j]:
                        new_line[j] = new_line[j].replace(remove[k], '')

            for i in range(len(new_line)):
                lst = new_line[i].split(' ')
                for j in range(len(lst)):
                    rep_string = lst[j][0].upper()
                    lst[j] = lst[j].replace(lst[j][0],rep_string,1)
                new_line[i] = ' '.join(lst)
            
            if new_line[0].upper() == precName:
                x = new_line[0]+' '+new_line[2]+' '
                y = x+new_line[3]+' '+new_line[4]
                return y
    
    except FileNotFoundError:
        return 'File Not Found'

'''
The try/except ensures that a feesible file is used. If the file is not found
then the function will return 'File Not Found.

The initial for loop and the two lines above iterare through each line in the
spreadsheet. The first for loop assigns the correct amount of keys for each
city in the spreadsheet and each key is assigmed to an empty list.

The second for loop takes each precinct and adds it to the list which is
assigned to the corresponding city of that precinct.

The last for loop adds the number of precincts each city has to the end of
each respective list, and finally, the dictionary is returned.
'''
def pollingPrecincts(precFile):
    new_dict = {}
    try:
        file = open(precFile, 'r')
        file = file.readlines()
        for i in range(1, len(file)):
            new_line = file[i].split(',')
            if new_line[-2].lower() not in new_dict:
                new_dict[new_line[-2].lower()] = []
        for i in range(1, len(file)):
            new_line = file[i].split(',')
            add = new_line[0]
            new_dict[new_line[-2].lower()].append(add.lower())
        for i in new_dict:
            new_dict[i].append(len(new_dict[i]))
        
        return new_dict
    
    except FileNotFoundError:
        return 'File Not Found'
    
'''
The initial for loop goes through each 3rd element in the list starting at the
3rd element.

The try statement has an if/else statement which checks if the length of the
zip code is not 5 digits. If it is not 5 digits, the zip code is stored as 0.

The except statement checks if there was a potential value error in the input
for the participation rate. If there is an error, the participation rate is
stored as 0.
'''
def voter_data(flat_data):
    new_list = []
    for i in range(2, len(flat_data), 3):
        try:
            if len(flat_data[i]) == 5:
                new_list.append({'Full Name': flat_data[i-2],
                             'Participation Rate': float(flat_data[i-1]),
                             'Zip Code': int(flat_data[i])})
            else: 
                new_list.append({'Full Name': flat_data[i-2],
                             'Participation Rate': float(flat_data[i-1]),
                             'Zip Code': 0})
        except ValueError:
            new_list.append({'Full Name': flat_data[i-2],
                             'Participation Rate': 0,
                             'Zip Code': int(flat_data[i])})
            
    return new_list
