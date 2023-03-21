'''
-------------------------------------------------------------------------------
Name: Alexander Farouz
Assignment: PA 5
Due Date: 10/26/22
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
The variables declared in the code are list1, max_score, and j.
The list is initialized as empty, and all integer values are set = to 0.

The first for loop has an if statement which says for every 3 elements in
the parameter matches (which is a list) and if every third element in the
list is greater than or equal to 80, append a new empty list into list1.
This allows for a correct number of lists in a list for the final output.

The second for loop goes through the list 'matches' and contains an if
statement which takes every third element of the list. If this statement is
considered true, there are 2 more if statements inside of this if statement.

The first if statement finds the maximum integer value and stores it in
the variable max_score for later (this will determine where to put the
heart in the final list).

The second if statement checks if the value is greater than or equal to 80.
If it is, the if statement contains a while loop which says if j is less
than the length of list1 (the list with currently empty lists), than add
the current integer value and the two preceding elements in the input list
matches. There is a counter at the end which increments j by 1. J
represents each time an empty list in list1 is appended. This is followed
by a break statement to reset the for loop. This is essential because
if it were not there, the first list would be as long as the input list
matches and the other empty lists in list1 would remain empty. The break
statement makes it so that the other lists are appended with the
corresponding elements.

Finally there is a for loop in a for loop that goes through list1 now with
list with the proper elements inside it, and finds the list with the
max_score value inside of the list, and appends the heart symbol to the
end of the inner list containing max_score.

To assign this list to the parameter, matches is cleared with .clear()
making it empty, then list1 is added to matches with .extend() 
'''
def findRecommendations(matches):
    list1 = []
    max_score = 0
    j = 0
    for i in range(len(matches)):
        if (i + 1) % 3  == 0 and matches[i] >= 80:
            list1.append([])
    for i in range(len(matches)):
        if (i + 1) % 3  == 0:
            if matches[i] > max_score:
                max_score = matches[i]
            if matches[i] >= 80:
                while j < len(list1):
                    list1[j].append(matches[i - 2])
                    list1[j].append(matches[i - 1])
                    list1[j].append(matches[i])
                    j += 1
                    break
                    
    for i in range(len(list1)):
        for j in list1[i]:
            if max_score == j:
                list1[i].append("\u2665")
                
    matches.clear()
    matches.extend(list1)
    
'''
The lists declared in the code are list1, list2, list3, int_list, and
master_list, all initialized as empty lists.

The first for loop goes through the parameter list, datingTrack, which
contains lists inside of it. The first value of these lists are appended to
list1.

The second for loop goes through list1 and appends all values which do not
repeat into list2, essentially recreating list1 without duplicates.

The third for loop appends an empty list to list3 for each value in list2.
In other words, the length of list3 is equal to the length of list2 and is
full of empty lists.

The fourth for loop appends each value in list2, including the duplicate
values in list1, into their own list. For example, if list1 is:
[B333, B444, B444, B333, B555], list3 would look like:
[[B333, B333], [B444, B444], [B555]].

The fifth for loop goes through the lists in list3, and takes the length
of these lists, appending the integer value into int_list. So int_list
contains the integer values for the length of each list in list3, which
can also represent the number of times the ID was present in datingTrack

The sixth for loop takes takes the length of list 2 and appends a
corresponding number of empty tuples to master_list. Each empty
tuple represents a each unique ID code in datingTrack.

The seventh and final for loop goes through the length of master_list
and adds the ID codes from list2 and the corresponding number of times
that same ID code was in datingTrack to the empty tuples, making
master_list our final result.

datingTrack is then cleared with .clear() and master_list is added to
it with .extend.
'''
def compressInfo(datingTrack):
    list1 = []
    list2 = []
    list3 = []
    int_list = []
    master_list = []
    for i in range(len(datingTrack)):
        list1.append(datingTrack[i][0])
    
    for i in range(len(list1)):
        for j in range(len(list1)):
            if list1[i] != list1[j] and list1[i] not in list2:
                list2.append(list1[i])
            elif list1[i] == list1[j] and i == j and list1[i] not in list2:
                list2.append(list1[i])
    
    for i in range(len(list2)):
        list3.append([])
    
    for i in range(len(list2)):
        for j in range(len(list1)):
            if list2[i] == list1[j] and i != j:
                list3[i].append(list2[i])
            elif list2[i] == list1[j] and i == j and list3[i] == []:
                list3[i].append(list2[i])
    
    for i in range(len(list3)):
        for j in list3[i]:
            int_list.append(len(list3[i]))
            break
        
    for i in range(len(list2)):
        master_list.append(())
    
    for i in range(len(master_list)):
        master_list[i] += (list2[i],)
        master_list[i] += (int_list[i],)
                        
    
    datingTrack.clear()
    datingTrack.extend(master_list)

'''
The following code contains nested 4 for loops, with an if statement inside
the last, innermost for loop.

The first parameter is a list of lists, and the second parameter is a list of
tuples, allowing iteration in each of the parameters, hence the 4 for loops.

The if statement is true if the position in the inner list[i] in profileInfo
is equal to the inner tuple[k] in datingTrack and the second element in
datingTrack[k] is not in profileInfo[i]. If this is true then the second
element in datingTrack[k] is apended to profileInfo[i].
'''
def combineInfo(profileInfo, datingTrack):
    for i in range(len(profileInfo)):
        for j in profileInfo[i]:
            for k in range(len(datingTrack)):
                for l in datingTrack[k]:
                    if j == l and datingTrack[k][1] not in profileInfo[i]:
                        profileInfo[i].append(datingTrack[k][1])
                                 

'''
The code decleares 1 empty set called set1

There are 2 nested for loops which go through the values assigned to the
dict parameter called profiles.

Inside the innermost for loop, there is an if statement which checks if the
value assigned to profile i is eqaul to the location parameter. If this
statement is true, the name to which the location is assigned to in the
profile parameter is added to set1.
'''
def setofNames(profiles, location):
    set1 = set({})
    for i in profiles:
        for j in profiles[i]:
            if j == location:
                set1.add(profiles[i][0])
    return set1



